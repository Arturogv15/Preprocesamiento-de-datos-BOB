<<<<<<< HEAD
# Project Dependencies

This document lists all the required dependencies for the Data Preprocessing Educational Platform.

## Python Dependencies (requirements.txt)

### Core Flask
```
Flask==2.3.3
Flask-SQLAlchemy==3.0.5
Flask-Login==0.6.2
Flask-Bcrypt==1.0.1
Flask-Migrate==4.0.5
Flask-CORS==4.0.0
```

### Data Processing
```
pandas==2.0.3
numpy==1.24.3
scikit-learn==1.3.0
scipy==1.11.1
```

### Visualization
```
matplotlib==3.7.2
seaborn==0.12.2
plotly==5.16.1
kaleido==0.2.1
```

### Database
```
SQLAlchemy==2.0.20
psycopg2-binary==2.9.7
```

### Utilities
```
python-dotenv==1.0.0
Werkzeug==2.3.7
Jinja2==3.1.2
```

### File Handling
```
openpyxl==3.1.2
xlrd==2.0.1
```

### Testing (Development)
```
pytest==7.4.0
pytest-flask==1.2.0
pytest-cov==4.1.0
```

### Code Quality (Development)
```
flake8==6.1.0
black==23.7.0
pylint==2.17.5
```

### Production Server
```
gunicorn==21.2.0
```

## Frontend Dependencies (CDN Links)

### CSS Frameworks
- Bootstrap 5.3.0: `https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css`
- Font Awesome 6.4.0: `https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css`

### JavaScript Libraries
- Bootstrap JS 5.3.0: `https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js`
- jQuery 3.7.0: `https://code.jquery.com/jquery-3.7.0.min.js`
- Chart.js 4.3.0: `https://cdn.jsdelivr.net/npm/chart.js@4.3.0/dist/chart.umd.js`
- Plotly.js 2.24.2: `https://cdn.plot.ly/plotly-2.24.2.min.js`
- DataTables 1.13.5: `https://cdn.datatables.net/1.13.5/js/jquery.dataTables.min.js`
- DataTables CSS: `https://cdn.datatables.net/1.13.5/css/jquery.dataTables.min.css`

## Installation Instructions

### 1. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 3. Verify Installation
```bash
python -c "import flask; import pandas; import sklearn; print('All dependencies installed successfully!')"
```

## Version Compatibility

- **Python**: 3.9 or higher required
- **Node.js**: Not required (using CDN for frontend libraries)
- **Database**: SQLite 3.x (development), PostgreSQL 12+ (production)

## Optional Dependencies

### For Advanced Features
```
redis==4.6.0  # For caching
celery==5.3.1  # For background tasks
```

### For Documentation
```
sphinx==7.1.2
sphinx-rtd-theme==1.3.0
```

## Development Tools

### Recommended IDE Extensions
- Python (Microsoft)
- Pylance
- Python Test Explorer
- GitLens
- Prettier
- ESLint

### Database Tools
- DB Browser for SQLite (development)
- pgAdmin (PostgreSQL production)
- DBeaver (universal)

## System Requirements

### Minimum
- RAM: 2GB
- Disk Space: 10GB
- CPU: Dual-core processor

### Recommended
- RAM: 4GB or more
- Disk Space: 20GB
- CPU: Quad-core processor
- SSD for better performance

## Troubleshooting

### Common Installation Issues

**Issue**: `pip install` fails for scikit-learn
**Solution**: Install build tools
```bash
# Windows
pip install --upgrade setuptools wheel
# Linux
sudo apt-get install python3-dev
# macOS
xcode-select --install
```

**Issue**: matplotlib backend errors
**Solution**: Set backend in code
```python
import matplotlib
matplotlib.use('Agg')
```

**Issue**: psycopg2 installation fails
**Solution**: Use binary version
```bash
pip install psycopg2-binary
```

## Security Considerations

### Production Dependencies
- Keep all packages updated
- Use `pip-audit` to check for vulnerabilities
- Pin exact versions in production
- Use virtual environments

### Security Scanning
```bash
pip install pip-audit
pip-audit
```

## Performance Optimization

### Recommended Packages
```
ujson==5.8.0  # Faster JSON parsing
orjson==3.9.4  # Even faster JSON
```

### Caching
```
Flask-Caching==2.0.2
```

## License Information

All dependencies are open-source with permissive licenses:
- Flask: BSD-3-Clause
- pandas: BSD-3-Clause
- scikit-learn: BSD-3-Clause
- Bootstrap: MIT
- Chart.js: MIT

## Update Schedule

- **Security updates**: Immediate
- **Minor updates**: Monthly
- **Major updates**: Quarterly (with testing)

## Support

For dependency-related issues:
1. Check official documentation
2. Search GitHub issues
3. Stack Overflow
=======
# Project Dependencies

This document lists all the required dependencies for the Data Preprocessing Educational Platform.

## Python Dependencies (requirements.txt)

### Core Flask
```
Flask==2.3.3
Flask-SQLAlchemy==3.0.5
Flask-Login==0.6.2
Flask-Bcrypt==1.0.1
Flask-Migrate==4.0.5
Flask-CORS==4.0.0
```

### Data Processing
```
pandas==2.0.3
numpy==1.24.3
scikit-learn==1.3.0
scipy==1.11.1
```

### Visualization
```
matplotlib==3.7.2
seaborn==0.12.2
plotly==5.16.1
kaleido==0.2.1
```

### Database
```
SQLAlchemy==2.0.20
psycopg2-binary==2.9.7
```

### Utilities
```
python-dotenv==1.0.0
Werkzeug==2.3.7
Jinja2==3.1.2
```

### File Handling
```
openpyxl==3.1.2
xlrd==2.0.1
```

### Testing (Development)
```
pytest==7.4.0
pytest-flask==1.2.0
pytest-cov==4.1.0
```

### Code Quality (Development)
```
flake8==6.1.0
black==23.7.0
pylint==2.17.5
```

### Production Server
```
gunicorn==21.2.0
```

## Frontend Dependencies (CDN Links)

### CSS Frameworks
- Bootstrap 5.3.0: `https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css`
- Font Awesome 6.4.0: `https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css`

### JavaScript Libraries
- Bootstrap JS 5.3.0: `https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js`
- jQuery 3.7.0: `https://code.jquery.com/jquery-3.7.0.min.js`
- Chart.js 4.3.0: `https://cdn.jsdelivr.net/npm/chart.js@4.3.0/dist/chart.umd.js`
- Plotly.js 2.24.2: `https://cdn.plot.ly/plotly-2.24.2.min.js`
- DataTables 1.13.5: `https://cdn.datatables.net/1.13.5/js/jquery.dataTables.min.js`
- DataTables CSS: `https://cdn.datatables.net/1.13.5/css/jquery.dataTables.min.css`

## Installation Instructions

### 1. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 3. Verify Installation
```bash
python -c "import flask; import pandas; import sklearn; print('All dependencies installed successfully!')"
```

## Version Compatibility

- **Python**: 3.9 or higher required
- **Node.js**: Not required (using CDN for frontend libraries)
- **Database**: SQLite 3.x (development), PostgreSQL 12+ (production)

## Optional Dependencies

### For Advanced Features
```
redis==4.6.0  # For caching
celery==5.3.1  # For background tasks
```

### For Documentation
```
sphinx==7.1.2
sphinx-rtd-theme==1.3.0
```

## Development Tools

### Recommended IDE Extensions
- Python (Microsoft)
- Pylance
- Python Test Explorer
- GitLens
- Prettier
- ESLint

### Database Tools
- DB Browser for SQLite (development)
- pgAdmin (PostgreSQL production)
- DBeaver (universal)

## System Requirements

### Minimum
- RAM: 2GB
- Disk Space: 10GB
- CPU: Dual-core processor

### Recommended
- RAM: 4GB or more
- Disk Space: 20GB
- CPU: Quad-core processor
- SSD for better performance

## Troubleshooting

### Common Installation Issues

**Issue**: `pip install` fails for scikit-learn
**Solution**: Install build tools
```bash
# Windows
pip install --upgrade setuptools wheel
# Linux
sudo apt-get install python3-dev
# macOS
xcode-select --install
```

**Issue**: matplotlib backend errors
**Solution**: Set backend in code
```python
import matplotlib
matplotlib.use('Agg')
```

**Issue**: psycopg2 installation fails
**Solution**: Use binary version
```bash
pip install psycopg2-binary
```

## Security Considerations

### Production Dependencies
- Keep all packages updated
- Use `pip-audit` to check for vulnerabilities
- Pin exact versions in production
- Use virtual environments

### Security Scanning
```bash
pip install pip-audit
pip-audit
```

## Performance Optimization

### Recommended Packages
```
ujson==5.8.0  # Faster JSON parsing
orjson==3.9.4  # Even faster JSON
```

### Caching
```
Flask-Caching==2.0.2
```

## License Information

All dependencies are open-source with permissive licenses:
- Flask: BSD-3-Clause
- pandas: BSD-3-Clause
- scikit-learn: BSD-3-Clause
- Bootstrap: MIT
- Chart.js: MIT

## Update Schedule

- **Security updates**: Immediate
- **Minor updates**: Monthly
- **Major updates**: Quarterly (with testing)

## Support

For dependency-related issues:
1. Check official documentation
2. Search GitHub issues
3. Stack Overflow
>>>>>>> 5cacc14741e04989bfeb01a4c6f9a705353a88f4
4. Project issue tracker