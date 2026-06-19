import pandas as pd
import numpy as np
from sklearn.preprocessing import (
    MinMaxScaler, StandardScaler, RobustScaler, MaxAbsScaler,
    OneHotEncoder, LabelEncoder, OrdinalEncoder
)
from sklearn.impute import KNNImputer, SimpleImputer
from sklearn.decomposition import PCA
from sklearn.feature_selection import VarianceThreshold, SelectKBest, f_classif
from sklearn.ensemble import IsolationForest
from scipy import stats


class DataProcessor:
    """Handle all data preprocessing operations"""
    
    def __init__(self, dataframe):
        self.df = dataframe.copy()
        self.original_df = dataframe.copy()
    
    def get_statistics(self):
        """Get comprehensive dataset statistics"""
        stats = {
            'shape': self.df.shape,
            'columns': self.df.columns.tolist(),
            'dtypes': self.df.dtypes.astype(str).to_dict(),
            'missing_values': self.df.isnull().sum().to_dict(),
            'missing_percentage': (self.df.isnull().sum() / len(self.df) * 100).to_dict(),
            'duplicates': int(self.df.duplicated().sum()),
            'memory_usage': f"{self.df.memory_usage(deep=True).sum() / 1024**2:.2f} MB"
        }
        
        # Descriptive statistics for numerical columns
        numerical_cols = self.df.select_dtypes(include=[np.number]).columns
        if len(numerical_cols) > 0:
            stats['descriptive'] = self.df[numerical_cols].describe().to_dict()
        
        # Unique counts for categorical columns
        categorical_cols = self.df.select_dtypes(include=['object', 'category']).columns
        if len(categorical_cols) > 0:
            stats['unique_counts'] = {col: int(self.df[col].nunique()) for col in categorical_cols}
        
        return stats
    
    def impute_missing(self, method='mean', columns=None, **kwargs):
        """Impute missing values"""
        if columns is None:
            columns = self.df.columns[self.df.isnull().any()].tolist()
        
        missing_before = self.df[columns].isnull().sum().sum()
        
        for col in columns:
            if col not in self.df.columns:
                continue
            
            if method == 'mean':
                self.df[col].fillna(self.df[col].mean(), inplace=True)
            elif method == 'median':
                self.df[col].fillna(self.df[col].median(), inplace=True)
            elif method == 'mode':
                self.df[col].fillna(self.df[col].mode()[0], inplace=True)
            elif method == 'ffill':
                self.df[col].fillna(method='ffill', inplace=True)
            elif method == 'bfill':
                self.df[col].fillna(method='bfill', inplace=True)
            elif method == 'constant':
                fill_value = kwargs.get('fill_value', 0)
                self.df[col].fillna(fill_value, inplace=True)
            elif method == 'knn':
                n_neighbors = kwargs.get('n_neighbors', 5)
                imputer = KNNImputer(n_neighbors=n_neighbors)
                self.df[columns] = imputer.fit_transform(self.df[columns])
            elif method == 'drop':
                self.df.dropna(subset=[col], inplace=True)
        
        missing_after = self.df[columns].isnull().sum().sum()
        
        stats = {
            'columns_affected': columns,
            'missing_before': int(missing_before),
            'missing_after': int(missing_after),
            'rows_affected': int(missing_before - missing_after),
            'method': method
        }
        
        return self.df, stats
    
    def remove_duplicates(self, subset=None, keep='first'):
        """Remove duplicate rows"""
        duplicates_before = self.df.duplicated(subset=subset).sum()
        
        self.df.drop_duplicates(subset=subset, keep=keep, inplace=True)
        
        duplicates_after = self.df.duplicated(subset=subset).sum()
        
        stats = {
            'duplicates_removed': int(duplicates_before - duplicates_after),
            'rows_remaining': len(self.df),
            'subset': subset if subset else 'all columns',
            'keep': keep
        }
        
        return self.df, stats
    
    def handle_outliers(self, method='iqr', columns=None, action='remove', **kwargs):
        """Detect and handle outliers"""
        if columns is None:
            columns = self.df.select_dtypes(include=[np.number]).columns.tolist()
        
        outliers_mask = pd.Series([False] * len(self.df))
        outlier_counts = {}
        
        for col in columns:
            if col not in self.df.columns:
                continue
            
            if method == 'iqr':
                Q1 = self.df[col].quantile(0.25)
                Q3 = self.df[col].quantile(0.75)
                IQR = Q3 - Q1
                multiplier = kwargs.get('multiplier', 1.5)
                lower_bound = Q1 - multiplier * IQR
                upper_bound = Q3 + multiplier * IQR
                col_outliers = (self.df[col] < lower_bound) | (self.df[col] > upper_bound)
                
            elif method == 'zscore':
                threshold = kwargs.get('threshold', 3)
                z_scores = np.abs(stats.zscore(self.df[col].dropna()))
                col_outliers = pd.Series([False] * len(self.df))
                col_outliers[self.df[col].notna()] = z_scores > threshold
                
            elif method == 'isolation_forest':
                contamination = kwargs.get('contamination', 0.1)
                iso_forest = IsolationForest(contamination=contamination, random_state=42)
                predictions = iso_forest.fit_predict(self.df[[col]].fillna(self.df[col].mean()))
                col_outliers = predictions == -1
            
            else:
                continue
            
            outliers_mask |= col_outliers
            outlier_counts[col] = int(col_outliers.sum())
            
            # Apply action
            if action == 'remove':
                pass  # Will remove after loop
            elif action == 'cap':
                if method == 'iqr':
                    self.df.loc[self.df[col] < lower_bound, col] = lower_bound
                    self.df.loc[self.df[col] > upper_bound, col] = upper_bound
            elif action == 'flag':
                self.df[f'{col}_outlier'] = col_outliers
        
        rows_before = len(self.df)
        
        if action == 'remove':
            self.df = self.df[~outliers_mask]
        
        rows_after = len(self.df)
        
        stats = {
            'method': method,
            'action': action,
            'outliers_by_column': outlier_counts,
            'total_outliers': int(outliers_mask.sum()),
            'rows_removed': rows_before - rows_after if action == 'remove' else 0,
            'rows_remaining': rows_after
        }
        
        return self.df, stats
    
    def scale_features(self, method='minmax', columns=None, **kwargs):
        """Scale numerical features"""
        if columns is None:
            columns = self.df.select_dtypes(include=[np.number]).columns.tolist()
        
        # Select scaler
        if method == 'minmax':
            feature_range = kwargs.get('feature_range', (0, 1))
            scaler = MinMaxScaler(feature_range=feature_range)
        elif method == 'standard':
            scaler = StandardScaler()
        elif method == 'robust':
            scaler = RobustScaler()
        elif method == 'maxabs':
            scaler = MaxAbsScaler()
        else:
            raise ValueError(f"Unknown scaling method: {method}")
        
        # Store original values for comparison
        original_stats = self.df[columns].describe().to_dict()
        
        # Apply scaling
        self.df[columns] = scaler.fit_transform(self.df[columns])
        
        # New statistics
        scaled_stats = self.df[columns].describe().to_dict()
        
        stats = {
            'method': method,
            'columns_scaled': columns,
            'original_stats': original_stats,
            'scaled_stats': scaled_stats
        }
        
        return self.df, stats
    
    def encode_categorical(self, method='onehot', columns=None, **kwargs):
        """Encode categorical variables"""
        if columns is None:
            columns = self.df.select_dtypes(include=['object', 'category']).columns.tolist()
        
        encoded_columns = []
        
        for col in columns:
            if col not in self.df.columns:
                continue
            
            if method == 'onehot':
                # One-hot encoding
                dummies = pd.get_dummies(self.df[col], prefix=col, drop_first=kwargs.get('drop_first', False))
                self.df = pd.concat([self.df, dummies], axis=1)
                self.df.drop(col, axis=1, inplace=True)
                encoded_columns.extend(dummies.columns.tolist())
                
            elif method == 'label':
                # Label encoding
                le = LabelEncoder()
                self.df[col] = le.fit_transform(self.df[col].astype(str))
                encoded_columns.append(col)
                
            elif method == 'ordinal':
                # Ordinal encoding
                categories = kwargs.get('categories', None)
                if categories and col in categories:
                    oe = OrdinalEncoder(categories=[categories[col]])
                    self.df[col] = oe.fit_transform(self.df[[col]])
                else:
                    # Auto ordinal
                    self.df[col] = pd.Categorical(self.df[col]).codes
                encoded_columns.append(col)
        
        stats = {
            'method': method,
            'original_columns': columns,
            'encoded_columns': encoded_columns,
            'new_shape': self.df.shape
        }
        
        return self.df, stats
    
    def merge_datasets(self, other_df, how='inner', on=None, left_on=None, right_on=None):
        """Merge with another dataset"""
        rows_before = len(self.df)
        cols_before = len(self.df.columns)
        
        self.df = pd.merge(
            self.df, other_df,
            how=how,
            on=on,
            left_on=left_on,
            right_on=right_on
        )
        
        rows_after = len(self.df)
        cols_after = len(self.df.columns)
        
        stats = {
            'merge_type': how,
            'rows_before': rows_before,
            'rows_after': rows_after,
            'columns_before': cols_before,
            'columns_after': cols_after,
            'rows_added': rows_after - rows_before,
            'columns_added': cols_after - cols_before
        }
        
        return self.df, stats
    
    def apply_pca(self, n_components=2, columns=None):
        """Apply PCA for dimensionality reduction"""
        if columns is None:
            columns = self.df.select_dtypes(include=[np.number]).columns.tolist()
        
        # Standardize features before PCA
        scaler = StandardScaler()
        scaled_data = scaler.fit_transform(self.df[columns])
        
        # Apply PCA
        pca = PCA(n_components=n_components)
        principal_components = pca.fit_transform(scaled_data)
        
        # Create new dataframe with principal components
        pc_columns = [f'PC{i+1}' for i in range(n_components)]
        pc_df = pd.DataFrame(data=principal_components, columns=pc_columns)
        
        # Add to original dataframe
        self.df = pd.concat([self.df.reset_index(drop=True), pc_df], axis=1)
        
        stats = {
            'n_components': n_components,
            'explained_variance': pca.explained_variance_ratio_.tolist(),
            'cumulative_variance': np.cumsum(pca.explained_variance_ratio_).tolist(),
            'original_features': columns,
            'new_features': pc_columns
        }
        
        return self.df, stats
    
    def select_features(self, method='variance', n_features=10, **kwargs):
        """Select most important features"""
        numerical_cols = self.df.select_dtypes(include=[np.number]).columns.tolist()
        
        if method == 'variance':
            threshold = kwargs.get('threshold', 0.0)
            selector = VarianceThreshold(threshold=threshold)
            selector.fit(self.df[numerical_cols])
            selected_features = [col for col, selected in zip(numerical_cols, selector.get_support()) if selected]
            
        elif method == 'correlation':
            target = kwargs.get('target')
            if target and target in self.df.columns:
                correlations = self.df[numerical_cols].corrwith(self.df[target]).abs()
                selected_features = correlations.nlargest(n_features).index.tolist()
            else:
                # Select based on correlation with first column
                correlations = self.df[numerical_cols].corr().iloc[0].abs()
                selected_features = correlations.nlargest(n_features).index.tolist()
        
        elif method == 'kbest':
            target = kwargs.get('target')
            if target and target in self.df.columns:
                X = self.df[numerical_cols]
                y = self.df[target]
                selector = SelectKBest(f_classif, k=min(n_features, len(numerical_cols)))
                selector.fit(X, y)
                selected_features = [col for col, selected in zip(numerical_cols, selector.get_support()) if selected]
            else:
                selected_features = numerical_cols[:n_features]
        
        else:
            selected_features = numerical_cols[:n_features]
        
        stats = {
            'method': method,
            'original_features': len(numerical_cols),
            'selected_features': len(selected_features),
            'feature_names': selected_features
        }
        
        return selected_features, stats
    
    def reset(self):
        """Reset to original dataframe"""
        self.df = self.original_df.copy()
        return self.df

# Made with Bob
