
# Data Preprocessing Educational Platform

An interactive web application designed for teaching data preprocessing concepts in data mining courses. Students can learn theory, practice techniques with real datasets, take quizzes, and track their progress.

## 🎯 Project Overview

This platform provides a comprehensive learning environment for data preprocessing, covering:
- **Data Cleaning**: Missing value imputation, duplicate removal, outlier detection
- **Data Transformation**: Normalization, standardization, encoding
- **Data Integration**: Joins, merging, concatenation
- **Dimensionality Reduction**: PCA, feature selection

## ✨ Key Features

### 📚 Theory Modules
- Comprehensive content for each preprocessing topic
- Real-world examples and best practices
- Interactive diagrams and visualizations
- Code examples in Python

### 🔬 Practice Lab
- Interactive data preprocessing workspace
- Pre-loaded datasets (Titanic, Housing, Iris, etc.)
- Upload custom datasets (CSV, Excel, JSON)
- Real-time data preview and statistics
- Step-by-step preprocessing pipeline
- Undo/Redo functionality
- Export processed data

### 📊 Exploratory Data Analysis
- Statistical summaries
- Box plots for outlier detection
- Histograms and distribution plots
- Scatter plots for relationships
- Correlation heatmaps
- Missing data visualizations
- Pair plots

### 🎓 Quiz System
- Multiple choice questions
- Scenario-based problems
- Immediate feedback with explanations
- Progress tracking
- Score history

### 👤 User Management
- User registration and authentication
- Personal dashboard
- Progress tracking across modules
- Save and load preprocessing pipelines
- View quiz history

## 🛠️ Technology Stack

### Backend
- **Framework**: Flask (Python 3.9+)
- **Database**: SQLite (dev) / PostgreSQL (prod)
- **ORM**: SQLAlchemy
- **Authentication**: Flask-Login + Flask-Bcrypt
- **Data Processing**: pandas, numpy, scikit-learn
- **Visualization**: matplotlib, seaborn, plotly

### Frontend
- **Core**: HTML5, CSS3, JavaScript (ES6+)
- **UI Framework**: Bootstrap 5
- **Charts**: Plotly.js, Chart.js
- **Data Tables**: DataTables.js

## 📁 Project Structure

```
Preprocesamiento/
├── app/
│   ├── __init__.py              # Flask app initialization
│   ├── models.py                # Database models
│   ├── auth.py                  # Authentication routes
│   ├── routes.py                # Main application routes
│   ├── data_processing.py       # Data preprocessing logic
│   ├── visualization.py         # Visualization generation
│   └── quiz.py                  # Quiz management
├── static/
│   ├── css/                     # Stylesheets
│   ├── js/                      # JavaScript files
│   └── datasets/                # Pre-loaded datasets
├── templates/
│   ├── base.html                # Base template
│   ├── index.html               # Landing page
│   ├── theory/                  # Theory module templates
│   ├── practice/                # Practice lab templates
│   └── quiz/                    # Quiz templates
├── uploads/                     # Temporary user uploads
├── config.py                    # Configuration settings
├── requirements.txt             # Python dependencies
├── run.py                       # Application entry point
├── README.md                    # This file
├── PROJECT_PLAN.md              # Detailed project plan
├── TECHNICAL_SPECS.md           # Technical specifications
└── IMPLEMENTATION_ROADMAP.md    # 8-week implementation plan
```

## 🚀 Getting Started

### Prerequisites
- Python 3.9 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Installation

1. **Clone the repository**
```bash
git clone <repository-url>
cd Preprocesamiento
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
```bash
# Create .env file
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///app.db
FLASK_ENV=development
```

5. **Initialize database**
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

6. **Download sample datasets**
```bash
python scripts/download_datasets.py
```

7. **Run the application**
```bash
python run.py
```

8. **Access the application**
Open your browser and navigate to `http://localhost:5000`

## 📖 Documentation

- **[Project Plan](PROJECT_PLAN.md)**: Comprehensive project overview and features
- **[Technical Specifications](TECHNICAL_SPECS.md)**: Detailed API and implementation specs
- **[Implementation Roadmap](IMPLEMENTATION_ROADMAP.md)**: 8-week development timeline

## 🎓 Usage Guide

### For Students

1. **Register an account** on the landing page
2. **Start with Theory**: Read through the theory modules to understand concepts
3. **Practice in the Lab**: 
   - Select a pre-loaded dataset or upload your own
   - Explore the data using EDA tools
   - Apply preprocessing techniques
   - Visualize the results
   - Export processed data
4. **Test your knowledge**: Take quizzes to assess understanding
5. **Track progress**: Monitor your learning journey on the dashboard

### For Instructors

1. **Monitor student progress** through the admin dashboard
2. **Review quiz results** to identify areas needing attention
3. **Add custom datasets** for specific exercises
4. **Create new quiz questions** to expand assessment coverage

## 🔧 Development

### Running Tests
```bash
pytest tests/
```

### Code Style
```bash
flake8 app/
black app/
```

### Database Migrations
```bash
flask db migrate -m "Description of changes"
flask db upgrade
```

## 📊 Pre-loaded Datasets

The platform includes several curated datasets:

1. **Titanic Dataset** (~900 rows)
   - Passenger survival data
   - Mixed data types
   - Missing values present

2. **Housing Prices** (~1,500 rows)
   - Real estate data
   - Numerical features
   - Outliers present

3. **Iris Dataset** (150 rows)
   - Flower measurements
   - Clean, simple dataset
   - Good for beginners

4. **Customer Churn** (~7,000 rows)
   - Telecom customer data
   - Imbalanced classes
   - Business context

5. **Wine Quality** (~6,500 rows)
   - Wine characteristics
   - Multiple features
   - Good for PCA

6. **Adult Income** (~32,000 rows)
   - Census data
   - Many categorical variables
   - Large dataset

## 🎯 Learning Objectives

After completing this course, students will be able to:

- ✅ Identify and handle missing data appropriately
- ✅ Detect and remove duplicate records
- ✅ Identify and treat outliers using various methods
- ✅ Apply appropriate normalization and standardization techniques
- ✅ Encode categorical variables correctly
- ✅ Merge and integrate data from multiple sources
- ✅ Reduce dimensionality using PCA and feature selection
- ✅ Perform exploratory data analysis
- ✅ Build complete preprocessing pipelines

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Authors

- **Project Team** - Initial work and development

## 🙏 Acknowledgments

- Dataset sources: Kaggle, UCI Machine Learning Repository
- Inspiration: Data mining and preprocessing best practices
- Libraries: pandas, scikit-learn, Flask, Bootstrap

## 📧 Support

For questions or issues:
- Open an issue on GitHub
- Contact the development team
- Check the documentation

## 🗺️ Roadmap

### Version 1.0 (Current)
- ✅ Core preprocessing features
- ✅ Theory modules
- ✅ Quiz system
- ✅ Progress tracking

### Version 1.1 (Planned)
- [ ] Advanced ML preprocessing techniques
- [ ] Collaborative features
- [ ] Export to Jupyter notebooks
- [ ] Video tutorials

### Version 2.0 (Future)
- [ ] Integration with Google Colab
- [ ] Mobile app
- [ ] Multi-language support
- [ ] Discussion forum

## 📈 Project Status

**Current Phase**: Planning Complete ✅

**Next Steps**: 
1. Review and approve this plan
2. Switch to Code mode for implementation
3. Begin Week 1 tasks (Foundation & Setup)

## 🎨 Screenshots

*Screenshots will be added after implementation*

## 🔗 Useful Links

- [Flask Documentation](https://flask.palletsprojects.com/)
- [pandas Documentation](https://pandas.pydata.org/docs/)
- [scikit-learn Documentation](https://scikit-learn.org/stable/)
- [Bootstrap Documentation](https://getbootstrap.com/docs/)

---

=======
# Data Preprocessing Educational Platform

An interactive web application designed for teaching data preprocessing concepts in data mining courses. Students can learn theory, practice techniques with real datasets, take quizzes, and track their progress.

## 🎯 Project Overview

This platform provides a comprehensive learning environment for data preprocessing, covering:
- **Data Cleaning**: Missing value imputation, duplicate removal, outlier detection
- **Data Transformation**: Normalization, standardization, encoding
- **Data Integration**: Joins, merging, concatenation
- **Dimensionality Reduction**: PCA, feature selection

## ✨ Key Features

### 📚 Theory Modules
- Comprehensive content for each preprocessing topic
- Real-world examples and best practices
- Interactive diagrams and visualizations
- Code examples in Python

### 🔬 Practice Lab
- Interactive data preprocessing workspace
- Pre-loaded datasets (Titanic, Housing, Iris, etc.)
- Upload custom datasets (CSV, Excel, JSON)
- Real-time data preview and statistics
- Step-by-step preprocessing pipeline
- Undo/Redo functionality
- Export processed data

### 📊 Exploratory Data Analysis
- Statistical summaries
- Box plots for outlier detection
- Histograms and distribution plots
- Scatter plots for relationships
- Correlation heatmaps
- Missing data visualizations
- Pair plots

### 🎓 Quiz System
- Multiple choice questions
- Scenario-based problems
- Immediate feedback with explanations
- Progress tracking
- Score history

### 👤 User Management
- User registration and authentication
- Personal dashboard
- Progress tracking across modules
- Save and load preprocessing pipelines
- View quiz history

## 🛠️ Technology Stack

### Backend
- **Framework**: Flask (Python 3.9+)
- **Database**: SQLite (dev) / PostgreSQL (prod)
- **ORM**: SQLAlchemy
- **Authentication**: Flask-Login + Flask-Bcrypt
- **Data Processing**: pandas, numpy, scikit-learn
- **Visualization**: matplotlib, seaborn, plotly

### Frontend
- **Core**: HTML5, CSS3, JavaScript (ES6+)
- **UI Framework**: Bootstrap 5
- **Charts**: Plotly.js, Chart.js
- **Data Tables**: DataTables.js

## 📁 Project Structure

```
Preprocesamiento/
├── app/
│   ├── __init__.py              # Flask app initialization
│   ├── models.py                # Database models
│   ├── auth.py                  # Authentication routes
│   ├── routes.py                # Main application routes
│   ├── data_processing.py       # Data preprocessing logic
│   ├── visualization.py         # Visualization generation
│   └── quiz.py                  # Quiz management
├── static/
│   ├── css/                     # Stylesheets
│   ├── js/                      # JavaScript files
│   └── datasets/                # Pre-loaded datasets
├── templates/
│   ├── base.html                # Base template
│   ├── index.html               # Landing page
│   ├── theory/                  # Theory module templates
│   ├── practice/                # Practice lab templates
│   └── quiz/                    # Quiz templates
├── uploads/                     # Temporary user uploads
├── config.py                    # Configuration settings
├── requirements.txt             # Python dependencies
├── run.py                       # Application entry point
├── README.md                    # This file
├── PROJECT_PLAN.md              # Detailed project plan
├── TECHNICAL_SPECS.md           # Technical specifications
└── IMPLEMENTATION_ROADMAP.md    # 8-week implementation plan
```

## 🚀 Getting Started

### Prerequisites
- Python 3.9 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Installation

1. **Clone the repository**
```bash
git clone <repository-url>
cd Preprocesamiento
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
```bash
# Create .env file
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///app.db
FLASK_ENV=development
```

5. **Initialize database**
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

6. **Download sample datasets**
```bash
python scripts/download_datasets.py
```

7. **Run the application**
```bash
python run.py
```

8. **Access the application**
Open your browser and navigate to `http://localhost:5000`

## 📖 Documentation

- **[Project Plan](PROJECT_PLAN.md)**: Comprehensive project overview and features
- **[Technical Specifications](TECHNICAL_SPECS.md)**: Detailed API and implementation specs
- **[Implementation Roadmap](IMPLEMENTATION_ROADMAP.md)**: 8-week development timeline

## 🎓 Usage Guide

### For Students

1. **Register an account** on the landing page
2. **Start with Theory**: Read through the theory modules to understand concepts
3. **Practice in the Lab**: 
   - Select a pre-loaded dataset or upload your own
   - Explore the data using EDA tools
   - Apply preprocessing techniques
   - Visualize the results
   - Export processed data
4. **Test your knowledge**: Take quizzes to assess understanding
5. **Track progress**: Monitor your learning journey on the dashboard

### For Instructors

1. **Monitor student progress** through the admin dashboard
2. **Review quiz results** to identify areas needing attention
3. **Add custom datasets** for specific exercises
4. **Create new quiz questions** to expand assessment coverage

## 🔧 Development

### Running Tests
```bash
pytest tests/
```

### Code Style
```bash
flake8 app/
black app/
```

### Database Migrations
```bash
flask db migrate -m "Description of changes"
flask db upgrade
```

## 📊 Pre-loaded Datasets

The platform includes several curated datasets:

1. **Titanic Dataset** (~900 rows)
   - Passenger survival data
   - Mixed data types
   - Missing values present

2. **Housing Prices** (~1,500 rows)
   - Real estate data
   - Numerical features
   - Outliers present

3. **Iris Dataset** (150 rows)
   - Flower measurements
   - Clean, simple dataset
   - Good for beginners

4. **Customer Churn** (~7,000 rows)
   - Telecom customer data
   - Imbalanced classes
   - Business context

5. **Wine Quality** (~6,500 rows)
   - Wine characteristics
   - Multiple features
   - Good for PCA

6. **Adult Income** (~32,000 rows)
   - Census data
   - Many categorical variables
   - Large dataset

## 🎯 Learning Objectives

After completing this course, students will be able to:

- ✅ Identify and handle missing data appropriately
- ✅ Detect and remove duplicate records
- ✅ Identify and treat outliers using various methods
- ✅ Apply appropriate normalization and standardization techniques
- ✅ Encode categorical variables correctly
- ✅ Merge and integrate data from multiple sources
- ✅ Reduce dimensionality using PCA and feature selection
- ✅ Perform exploratory data analysis
- ✅ Build complete preprocessing pipelines

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Authors

- **Project Team** - Initial work and development

## 🙏 Acknowledgments

- Dataset sources: Kaggle, UCI Machine Learning Repository
- Inspiration: Data mining and preprocessing best practices
- Libraries: pandas, scikit-learn, Flask, Bootstrap

## 📧 Support

For questions or issues:
- Open an issue on GitHub
- Contact the development team
- Check the documentation

## 🗺️ Roadmap

### Version 1.0 (Current)
- ✅ Core preprocessing features
- ✅ Theory modules
- ✅ Quiz system
- ✅ Progress tracking

### Version 1.1 (Planned)
- [ ] Advanced ML preprocessing techniques
- [ ] Collaborative features
- [ ] Export to Jupyter notebooks
- [ ] Video tutorials

### Version 2.0 (Future)
- [ ] Integration with Google Colab
- [ ] Mobile app
- [ ] Multi-language support
- [ ] Discussion forum

## 📈 Project Status

**Current Phase**: Planning Complete ✅

**Next Steps**: 
1. Review and approve this plan
2. Switch to Code mode for implementation
3. Begin Week 1 tasks (Foundation & Setup)

## 🎨 Screenshots

*Screenshots will be added after implementation*

## 🔗 Useful Links

- [Flask Documentation](https://flask.palletsprojects.com/)
- [pandas Documentation](https://pandas.pydata.org/docs/)
- [scikit-learn Documentation](https://scikit-learn.org/stable/)
- [Bootstrap Documentation](https://getbootstrap.com/docs/)

