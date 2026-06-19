<<<<<<< HEAD
"""
Script to download and prepare sample datasets for the preprocessing platform.
Downloads popular datasets from online repositories and saves them in the datasets folder.
"""

import os
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris, load_wine, load_breast_cancer
import urllib.request
import json

# Create datasets directory if it doesn't exist
DATASETS_DIR = 'datasets'
os.makedirs(DATASETS_DIR, exist_ok=True)

def download_iris():
    """Download and save Iris dataset"""
    print("Downloading Iris dataset...")
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
    
    # Add some missing values for practice
    df.loc[np.random.choice(df.index, 10), 'sepal length (cm)'] = np.nan
    df.loc[np.random.choice(df.index, 5), 'petal width (cm)'] = np.nan
    
    filepath = os.path.join(DATASETS_DIR, 'iris.csv')
    df.to_csv(filepath, index=False)
    print(f"[OK] Iris dataset saved to {filepath}")
    return df

def download_wine():
    """Download and save Wine dataset"""
    print("Downloading Wine dataset...")
    wine = load_wine()
    df = pd.DataFrame(wine.data, columns=wine.feature_names)
    df['wine_class'] = wine.target
    
    # Add some outliers and missing values
    df.loc[np.random.choice(df.index, 8), 'alcohol'] = np.nan
    df.loc[np.random.choice(df.index, 3), 'malic_acid'] = df['malic_acid'].max() * 2
    
    filepath = os.path.join(DATASETS_DIR, 'wine.csv')
    df.to_csv(filepath, index=False)
    print(f"[OK] Wine dataset saved to {filepath}")
    return df

def download_breast_cancer():
    """Download and save Breast Cancer dataset"""
    print("Downloading Breast Cancer dataset...")
    cancer = load_breast_cancer()
    df = pd.DataFrame(cancer.data, columns=cancer.feature_names)
    df['diagnosis'] = pd.Categorical.from_codes(cancer.target, ['malignant', 'benign'])
    
    # Add some missing values
    df.loc[np.random.choice(df.index, 15), 'mean radius'] = np.nan
    df.loc[np.random.choice(df.index, 10), 'mean texture'] = np.nan
    
    filepath = os.path.join(DATASETS_DIR, 'breast_cancer.csv')
    df.to_csv(filepath, index=False)
    print(f"[OK] Breast Cancer dataset saved to {filepath}")
    return df

def download_titanic():
    """Download Titanic dataset from GitHub"""
    print("Downloading Titanic dataset...")
    url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
    
    try:
        filepath = os.path.join(DATASETS_DIR, 'titanic.csv')
        urllib.request.urlretrieve(url, filepath)
        df = pd.read_csv(filepath)
        print(f"[OK] Titanic dataset saved to {filepath}")
        return df
    except Exception as e:
        print(f"[ERROR] Error downloading Titanic dataset: {e}")
        return None

def download_housing():
    """Download California Housing dataset"""
    print("Downloading California Housing dataset...")
    from sklearn.datasets import fetch_california_housing
    
    try:
        housing = fetch_california_housing()
        df = pd.DataFrame(housing.data, columns=housing.feature_names)
        df['MedHouseVal'] = housing.target
        
        # Add some missing values and outliers
        df.loc[np.random.choice(df.index, 100), 'MedInc'] = np.nan
        df.loc[np.random.choice(df.index, 50), 'HouseAge'] = np.nan
        
        filepath = os.path.join(DATASETS_DIR, 'california_housing.csv')
        df.to_csv(filepath, index=False)
        print(f"[OK] California Housing dataset saved to {filepath}")
        return df
    except Exception as e:
        print(f"[ERROR] Error downloading Housing dataset: {e}")
        return None

def create_customer_data():
    """Create a synthetic customer dataset with various data quality issues"""
    print("Creating synthetic customer dataset...")
    
    np.random.seed(42)
    n_samples = 1000
    
    # Generate customer data
    df = pd.DataFrame({
        'customer_id': range(1, n_samples + 1),
        'age': np.random.randint(18, 80, n_samples),
        'income': np.random.normal(50000, 20000, n_samples),
        'credit_score': np.random.randint(300, 850, n_samples),
        'account_balance': np.random.exponential(5000, n_samples),
        'num_transactions': np.random.poisson(20, n_samples),
        'customer_tenure_months': np.random.randint(1, 120, n_samples),
        'region': np.random.choice(['North', 'South', 'East', 'West'], n_samples),
        'account_type': np.random.choice(['Basic', 'Premium', 'Gold'], n_samples),
        'is_active': np.random.choice([True, False], n_samples, p=[0.8, 0.2])
    })
    
    # Add data quality issues
    # Missing values
    df.loc[np.random.choice(df.index, 50), 'income'] = np.nan
    df.loc[np.random.choice(df.index, 30), 'credit_score'] = np.nan
    df.loc[np.random.choice(df.index, 20), 'region'] = np.nan
    
    # Outliers
    df.loc[np.random.choice(df.index, 10), 'income'] = df['income'].max() * 5
    df.loc[np.random.choice(df.index, 5), 'account_balance'] = df['account_balance'].max() * 10
    
    # Duplicates
    duplicate_indices = np.random.choice(df.index, 20)
    df = pd.concat([df, df.loc[duplicate_indices]], ignore_index=True)
    
    # Inconsistent data
    df.loc[np.random.choice(df.index, 10), 'region'] = df.loc[np.random.choice(df.index, 10), 'region'].str.lower()
    
    filepath = os.path.join(DATASETS_DIR, 'customer_data.csv')
    df.to_csv(filepath, index=False)
    print(f"[OK] Customer dataset saved to {filepath}")
    return df

def create_sales_data():
    """Create a synthetic sales dataset for integration practice"""
    print("Creating synthetic sales dataset...")
    
    np.random.seed(42)
    n_samples = 500
    
    # Sales transactions
    sales_df = pd.DataFrame({
        'transaction_id': range(1, n_samples + 1),
        'customer_id': np.random.randint(1, 200, n_samples),
        'product_id': np.random.randint(1, 50, n_samples),
        'quantity': np.random.randint(1, 10, n_samples),
        'unit_price': np.random.uniform(10, 500, n_samples),
        'transaction_date': pd.date_range('2023-01-01', periods=n_samples, freq='D')
    })
    
    sales_df['total_amount'] = sales_df['quantity'] * sales_df['unit_price']
    
    # Product information
    products_df = pd.DataFrame({
        'product_id': range(1, 51),
        'product_name': [f'Product_{i}' for i in range(1, 51)],
        'category': np.random.choice(['Electronics', 'Clothing', 'Food', 'Books'], 50),
        'supplier_id': np.random.randint(1, 10, 50)
    })
    
    # Customer information
    customers_df = pd.DataFrame({
        'customer_id': range(1, 201),
        'customer_name': [f'Customer_{i}' for i in range(1, 201)],
        'city': np.random.choice(['New York', 'Los Angeles', 'Chicago', 'Houston'], 200),
        'state': np.random.choice(['NY', 'CA', 'IL', 'TX'], 200),
        'loyalty_tier': np.random.choice(['Bronze', 'Silver', 'Gold'], 200)
    })
    
    # Save datasets
    sales_df.to_csv(os.path.join(DATASETS_DIR, 'sales_transactions.csv'), index=False)
    products_df.to_csv(os.path.join(DATASETS_DIR, 'products.csv'), index=False)
    customers_df.to_csv(os.path.join(DATASETS_DIR, 'customers.csv'), index=False)
    
    print(f"[OK] Sales datasets saved to {DATASETS_DIR}")
    return sales_df, products_df, customers_df

def create_dataset_metadata():
    """Create metadata file describing all datasets"""
    metadata = {
        'iris.csv': {
            'name': 'Iris Dataset',
            'description': 'Classic dataset with measurements of iris flowers',
            'rows': 150,
            'columns': 5,
            'use_cases': ['Classification', 'Clustering', 'Visualization'],
            'has_missing': True,
            'has_outliers': False,
            'target': 'species'
        },
        'wine.csv': {
            'name': 'Wine Quality Dataset',
            'description': 'Chemical analysis of wines',
            'rows': 178,
            'columns': 14,
            'use_cases': ['Classification', 'Feature Selection'],
            'has_missing': True,
            'has_outliers': True,
            'target': 'wine_class'
        },
        'breast_cancer.csv': {
            'name': 'Breast Cancer Dataset',
            'description': 'Features computed from breast mass images',
            'rows': 569,
            'columns': 31,
            'use_cases': ['Classification', 'Dimensionality Reduction'],
            'has_missing': True,
            'has_outliers': False,
            'target': 'diagnosis'
        },
        'titanic.csv': {
            'name': 'Titanic Dataset',
            'description': 'Passenger data from the Titanic disaster',
            'rows': 891,
            'columns': 12,
            'use_cases': ['Classification', 'Data Cleaning', 'Feature Engineering'],
            'has_missing': True,
            'has_outliers': False,
            'target': 'Survived'
        },
        'california_housing.csv': {
            'name': 'California Housing Dataset',
            'description': 'Housing prices in California districts',
            'rows': 20640,
            'columns': 9,
            'use_cases': ['Regression', 'Feature Selection', 'Scaling'],
            'has_missing': True,
            'has_outliers': True,
            'target': 'MedHouseVal'
        },
        'customer_data.csv': {
            'name': 'Customer Data',
            'description': 'Synthetic customer data with quality issues',
            'rows': 1020,
            'columns': 10,
            'use_cases': ['Data Cleaning', 'Outlier Detection', 'Duplicate Removal'],
            'has_missing': True,
            'has_outliers': True,
            'target': 'is_active'
        },
        'sales_transactions.csv': {
            'name': 'Sales Transactions',
            'description': 'Sales transaction records',
            'rows': 500,
            'columns': 7,
            'use_cases': ['Data Integration', 'Time Series Analysis'],
            'has_missing': False,
            'has_outliers': False,
            'target': 'total_amount'
        },
        'products.csv': {
            'name': 'Product Catalog',
            'description': 'Product information for sales data',
            'rows': 50,
            'columns': 4,
            'use_cases': ['Data Integration', 'Joins'],
            'has_missing': False,
            'has_outliers': False,
            'target': None
        },
        'customers.csv': {
            'name': 'Customer Information',
            'description': 'Customer details for sales data',
            'rows': 200,
            'columns': 5,
            'use_cases': ['Data Integration', 'Joins'],
            'has_missing': False,
            'has_outliers': False,
            'target': None
        }
    }
    
    filepath = os.path.join(DATASETS_DIR, 'metadata.json')
    with open(filepath, 'w') as f:
        json.dump(metadata, f, indent=2)
    
    print(f"[OK] Metadata saved to {filepath}")

def main():
    """Download all datasets"""
    print("=" * 60)
    print("Downloading and preparing datasets...")
    print("=" * 60)
    
    # Download datasets
    download_iris()
    download_wine()
    download_breast_cancer()
    download_titanic()
    download_housing()
    
    # Create synthetic datasets
    create_customer_data()
    create_sales_data()
    
    # Create metadata
    create_dataset_metadata()
    
    print("=" * 60)
    print("[OK] All datasets downloaded successfully!")
    print(f"[OK] Datasets saved in: {os.path.abspath(DATASETS_DIR)}")
    print("=" * 60)
    
    # List all files
    print("\nAvailable datasets:")
    for file in sorted(os.listdir(DATASETS_DIR)):
        if file.endswith('.csv'):
            filepath = os.path.join(DATASETS_DIR, file)
            df = pd.read_csv(filepath)
            print(f"  - {file}: {len(df)} rows, {len(df.columns)} columns")

if __name__ == '__main__':
    main()

# Made with Bob
=======
"""
Script to download and prepare sample datasets for the preprocessing platform.
Downloads popular datasets from online repositories and saves them in the datasets folder.
"""

import os
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris, load_wine, load_breast_cancer
import urllib.request
import json

# Create datasets directory if it doesn't exist
DATASETS_DIR = 'datasets'
os.makedirs(DATASETS_DIR, exist_ok=True)

def download_iris():
    """Download and save Iris dataset"""
    print("Downloading Iris dataset...")
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
    
    # Add some missing values for practice
    df.loc[np.random.choice(df.index, 10), 'sepal length (cm)'] = np.nan
    df.loc[np.random.choice(df.index, 5), 'petal width (cm)'] = np.nan
    
    filepath = os.path.join(DATASETS_DIR, 'iris.csv')
    df.to_csv(filepath, index=False)
    print(f"[OK] Iris dataset saved to {filepath}")
    return df

def download_wine():
    """Download and save Wine dataset"""
    print("Downloading Wine dataset...")
    wine = load_wine()
    df = pd.DataFrame(wine.data, columns=wine.feature_names)
    df['wine_class'] = wine.target
    
    # Add some outliers and missing values
    df.loc[np.random.choice(df.index, 8), 'alcohol'] = np.nan
    df.loc[np.random.choice(df.index, 3), 'malic_acid'] = df['malic_acid'].max() * 2
    
    filepath = os.path.join(DATASETS_DIR, 'wine.csv')
    df.to_csv(filepath, index=False)
    print(f"[OK] Wine dataset saved to {filepath}")
    return df

def download_breast_cancer():
    """Download and save Breast Cancer dataset"""
    print("Downloading Breast Cancer dataset...")
    cancer = load_breast_cancer()
    df = pd.DataFrame(cancer.data, columns=cancer.feature_names)
    df['diagnosis'] = pd.Categorical.from_codes(cancer.target, ['malignant', 'benign'])
    
    # Add some missing values
    df.loc[np.random.choice(df.index, 15), 'mean radius'] = np.nan
    df.loc[np.random.choice(df.index, 10), 'mean texture'] = np.nan
    
    filepath = os.path.join(DATASETS_DIR, 'breast_cancer.csv')
    df.to_csv(filepath, index=False)
    print(f"[OK] Breast Cancer dataset saved to {filepath}")
    return df

def download_titanic():
    """Download Titanic dataset from GitHub"""
    print("Downloading Titanic dataset...")
    url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
    
    try:
        filepath = os.path.join(DATASETS_DIR, 'titanic.csv')
        urllib.request.urlretrieve(url, filepath)
        df = pd.read_csv(filepath)
        print(f"[OK] Titanic dataset saved to {filepath}")
        return df
    except Exception as e:
        print(f"[ERROR] Error downloading Titanic dataset: {e}")
        return None

def download_housing():
    """Download California Housing dataset"""
    print("Downloading California Housing dataset...")
    from sklearn.datasets import fetch_california_housing
    
    try:
        housing = fetch_california_housing()
        df = pd.DataFrame(housing.data, columns=housing.feature_names)
        df['MedHouseVal'] = housing.target
        
        # Add some missing values and outliers
        df.loc[np.random.choice(df.index, 100), 'MedInc'] = np.nan
        df.loc[np.random.choice(df.index, 50), 'HouseAge'] = np.nan
        
        filepath = os.path.join(DATASETS_DIR, 'california_housing.csv')
        df.to_csv(filepath, index=False)
        print(f"[OK] California Housing dataset saved to {filepath}")
        return df
    except Exception as e:
        print(f"[ERROR] Error downloading Housing dataset: {e}")
        return None

def create_customer_data():
    """Create a synthetic customer dataset with various data quality issues"""
    print("Creating synthetic customer dataset...")
    
    np.random.seed(42)
    n_samples = 1000
    
    # Generate customer data
    df = pd.DataFrame({
        'customer_id': range(1, n_samples + 1),
        'age': np.random.randint(18, 80, n_samples),
        'income': np.random.normal(50000, 20000, n_samples),
        'credit_score': np.random.randint(300, 850, n_samples),
        'account_balance': np.random.exponential(5000, n_samples),
        'num_transactions': np.random.poisson(20, n_samples),
        'customer_tenure_months': np.random.randint(1, 120, n_samples),
        'region': np.random.choice(['North', 'South', 'East', 'West'], n_samples),
        'account_type': np.random.choice(['Basic', 'Premium', 'Gold'], n_samples),
        'is_active': np.random.choice([True, False], n_samples, p=[0.8, 0.2])
    })
    
    # Add data quality issues
    # Missing values
    df.loc[np.random.choice(df.index, 50), 'income'] = np.nan
    df.loc[np.random.choice(df.index, 30), 'credit_score'] = np.nan
    df.loc[np.random.choice(df.index, 20), 'region'] = np.nan
    
    # Outliers
    df.loc[np.random.choice(df.index, 10), 'income'] = df['income'].max() * 5
    df.loc[np.random.choice(df.index, 5), 'account_balance'] = df['account_balance'].max() * 10
    
    # Duplicates
    duplicate_indices = np.random.choice(df.index, 20)
    df = pd.concat([df, df.loc[duplicate_indices]], ignore_index=True)
    
    # Inconsistent data
    df.loc[np.random.choice(df.index, 10), 'region'] = df.loc[np.random.choice(df.index, 10), 'region'].str.lower()
    
    filepath = os.path.join(DATASETS_DIR, 'customer_data.csv')
    df.to_csv(filepath, index=False)
    print(f"[OK] Customer dataset saved to {filepath}")
    return df

def create_sales_data():
    """Create a synthetic sales dataset for integration practice"""
    print("Creating synthetic sales dataset...")
    
    np.random.seed(42)
    n_samples = 500
    
    # Sales transactions
    sales_df = pd.DataFrame({
        'transaction_id': range(1, n_samples + 1),
        'customer_id': np.random.randint(1, 200, n_samples),
        'product_id': np.random.randint(1, 50, n_samples),
        'quantity': np.random.randint(1, 10, n_samples),
        'unit_price': np.random.uniform(10, 500, n_samples),
        'transaction_date': pd.date_range('2023-01-01', periods=n_samples, freq='D')
    })
    
    sales_df['total_amount'] = sales_df['quantity'] * sales_df['unit_price']
    
    # Product information
    products_df = pd.DataFrame({
        'product_id': range(1, 51),
        'product_name': [f'Product_{i}' for i in range(1, 51)],
        'category': np.random.choice(['Electronics', 'Clothing', 'Food', 'Books'], 50),
        'supplier_id': np.random.randint(1, 10, 50)
    })
    
    # Customer information
    customers_df = pd.DataFrame({
        'customer_id': range(1, 201),
        'customer_name': [f'Customer_{i}' for i in range(1, 201)],
        'city': np.random.choice(['New York', 'Los Angeles', 'Chicago', 'Houston'], 200),
        'state': np.random.choice(['NY', 'CA', 'IL', 'TX'], 200),
        'loyalty_tier': np.random.choice(['Bronze', 'Silver', 'Gold'], 200)
    })
    
    # Save datasets
    sales_df.to_csv(os.path.join(DATASETS_DIR, 'sales_transactions.csv'), index=False)
    products_df.to_csv(os.path.join(DATASETS_DIR, 'products.csv'), index=False)
    customers_df.to_csv(os.path.join(DATASETS_DIR, 'customers.csv'), index=False)
    
    print(f"[OK] Sales datasets saved to {DATASETS_DIR}")
    return sales_df, products_df, customers_df

def create_dataset_metadata():
    """Create metadata file describing all datasets"""
    metadata = {
        'iris.csv': {
            'name': 'Iris Dataset',
            'description': 'Classic dataset with measurements of iris flowers',
            'rows': 150,
            'columns': 5,
            'use_cases': ['Classification', 'Clustering', 'Visualization'],
            'has_missing': True,
            'has_outliers': False,
            'target': 'species'
        },
        'wine.csv': {
            'name': 'Wine Quality Dataset',
            'description': 'Chemical analysis of wines',
            'rows': 178,
            'columns': 14,
            'use_cases': ['Classification', 'Feature Selection'],
            'has_missing': True,
            'has_outliers': True,
            'target': 'wine_class'
        },
        'breast_cancer.csv': {
            'name': 'Breast Cancer Dataset',
            'description': 'Features computed from breast mass images',
            'rows': 569,
            'columns': 31,
            'use_cases': ['Classification', 'Dimensionality Reduction'],
            'has_missing': True,
            'has_outliers': False,
            'target': 'diagnosis'
        },
        'titanic.csv': {
            'name': 'Titanic Dataset',
            'description': 'Passenger data from the Titanic disaster',
            'rows': 891,
            'columns': 12,
            'use_cases': ['Classification', 'Data Cleaning', 'Feature Engineering'],
            'has_missing': True,
            'has_outliers': False,
            'target': 'Survived'
        },
        'california_housing.csv': {
            'name': 'California Housing Dataset',
            'description': 'Housing prices in California districts',
            'rows': 20640,
            'columns': 9,
            'use_cases': ['Regression', 'Feature Selection', 'Scaling'],
            'has_missing': True,
            'has_outliers': True,
            'target': 'MedHouseVal'
        },
        'customer_data.csv': {
            'name': 'Customer Data',
            'description': 'Synthetic customer data with quality issues',
            'rows': 1020,
            'columns': 10,
            'use_cases': ['Data Cleaning', 'Outlier Detection', 'Duplicate Removal'],
            'has_missing': True,
            'has_outliers': True,
            'target': 'is_active'
        },
        'sales_transactions.csv': {
            'name': 'Sales Transactions',
            'description': 'Sales transaction records',
            'rows': 500,
            'columns': 7,
            'use_cases': ['Data Integration', 'Time Series Analysis'],
            'has_missing': False,
            'has_outliers': False,
            'target': 'total_amount'
        },
        'products.csv': {
            'name': 'Product Catalog',
            'description': 'Product information for sales data',
            'rows': 50,
            'columns': 4,
            'use_cases': ['Data Integration', 'Joins'],
            'has_missing': False,
            'has_outliers': False,
            'target': None
        },
        'customers.csv': {
            'name': 'Customer Information',
            'description': 'Customer details for sales data',
            'rows': 200,
            'columns': 5,
            'use_cases': ['Data Integration', 'Joins'],
            'has_missing': False,
            'has_outliers': False,
            'target': None
        }
    }
    
    filepath = os.path.join(DATASETS_DIR, 'metadata.json')
    with open(filepath, 'w') as f:
        json.dump(metadata, f, indent=2)
    
    print(f"[OK] Metadata saved to {filepath}")

def main():
    """Download all datasets"""
    print("=" * 60)
    print("Downloading and preparing datasets...")
    print("=" * 60)
    
    # Download datasets
    download_iris()
    download_wine()
    download_breast_cancer()
    download_titanic()
    download_housing()
    
    # Create synthetic datasets
    create_customer_data()
    create_sales_data()
    
    # Create metadata
    create_dataset_metadata()
    
    print("=" * 60)
    print("[OK] All datasets downloaded successfully!")
    print(f"[OK] Datasets saved in: {os.path.abspath(DATASETS_DIR)}")
    print("=" * 60)
    
    # List all files
    print("\nAvailable datasets:")
    for file in sorted(os.listdir(DATASETS_DIR)):
        if file.endswith('.csv'):
            filepath = os.path.join(DATASETS_DIR, file)
            df = pd.read_csv(filepath)
            print(f"  - {file}: {len(df)} rows, {len(df.columns)} columns")

if __name__ == '__main__':
    main()

# Made with Bob
>>>>>>> 5cacc14741e04989bfeb01a4c6f9a705353a88f4
