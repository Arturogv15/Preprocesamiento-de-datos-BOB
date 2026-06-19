<<<<<<< HEAD
# Guía de Despliegue - Plataforma de Preprocesamiento

## 📋 Opciones de Despliegue

Esta guía cubre tres opciones de despliegue:
1. **Desarrollo Local** (para pruebas)
2. **Servidor Linux** (producción)
3. **Heroku** (cloud hosting)

## 1. Despliegue Local (Desarrollo)

### Requisitos
- Python 3.8+
- Git
- 2GB RAM mínimo

### Pasos

```bash
# 1. Clonar repositorio
git clone <repository-url>
cd Preprocesamiento

# 2. Crear entorno virtual
python -m venv venv

# Windows
.\venv\Scripts\activate

# Linux/Mac
source venv/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Configurar variables de entorno
cp .env.example .env
# Editar .env con tus configuraciones

# 5. Descargar datasets
python download_datasets.py

# 6. Inicializar base de datos
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

# 7. Ejecutar aplicación
python run.py
```

Accede a: `http://localhost:5000`

## 2. Despliegue en Servidor Linux

### Requisitos
- Ubuntu 20.04+ o similar
- Python 3.8+
- Nginx
- Supervisor (para gestión de procesos)
- PostgreSQL (recomendado para producción)

### Instalación de Dependencias

```bash
# Actualizar sistema
sudo apt update && sudo apt upgrade -y

# Instalar Python y herramientas
sudo apt install python3-pip python3-venv nginx supervisor postgresql postgresql-contrib -y

# Instalar dependencias del sistema para pandas/numpy
sudo apt install python3-dev libpq-dev build-essential -y
```

### Configuración de PostgreSQL

```bash
# Crear usuario y base de datos
sudo -u postgres psql

CREATE DATABASE preprocessing_db;
CREATE USER preprocessing_user WITH PASSWORD 'tu_contraseña_segura';
GRANT ALL PRIVILEGES ON DATABASE preprocessing_db TO preprocessing_user;
\q
```

### Configuración de la Aplicación

```bash
# Crear directorio de aplicación
sudo mkdir -p /var/www/preprocessing
sudo chown $USER:$USER /var/www/preprocessing

# Clonar repositorio
cd /var/www/preprocessing
git clone <repository-url> .

# Crear entorno virtual
python3 -m venv venv
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
pip install gunicorn psycopg2-binary

# Configurar variables de entorno
nano .env
```

**Contenido de .env para producción:**
```env
FLASK_APP=run.py
FLASK_ENV=production
SECRET_KEY=tu_clave_secreta_muy_larga_y_aleatoria
DATABASE_URL=postgresql://preprocessing_user:tu_contraseña_segura@localhost/preprocessing_db
UPLOAD_FOLDER=/var/www/preprocessing/uploads
DATASET_FOLDER=/var/www/preprocessing/datasets
MAX_CONTENT_LENGTH=16777216
```

```bash
# Descargar datasets
python download_datasets.py

# Inicializar base de datos
flask db upgrade

# Crear directorios necesarios
mkdir -p uploads datasets static/uploads
chmod 755 uploads datasets static/uploads
```

### Configuración de Gunicorn

Crear archivo de configuración:
```bash
nano gunicorn_config.py
```

```python
# gunicorn_config.py
bind = "127.0.0.1:8000"
workers = 4
worker_class = "sync"
worker_connections = 1000
timeout = 120
keepalive = 5
errorlog = "/var/www/preprocessing/logs/gunicorn_error.log"
accesslog = "/var/www/preprocessing/logs/gunicorn_access.log"
loglevel = "info"
```

```bash
# Crear directorio de logs
mkdir -p logs
```

### Configuración de Supervisor

```bash
sudo nano /etc/supervisor/conf.d/preprocessing.conf
```

```ini
[program:preprocessing]
directory=/var/www/preprocessing
command=/var/www/preprocessing/venv/bin/gunicorn -c gunicorn_config.py run:app
user=www-data
autostart=true
autorestart=true
stopasgroup=true
killasgroup=true
stderr_logfile=/var/www/preprocessing/logs/supervisor_error.log
stdout_logfile=/var/www/preprocessing/logs/supervisor_output.log
```

```bash
# Actualizar supervisor
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl start preprocessing
sudo supervisorctl status preprocessing
```

### Configuración de Nginx

```bash
sudo nano /etc/nginx/sites-available/preprocessing
```

```nginx
server {
    listen 80;
    server_name tu_dominio.com;  # Cambiar por tu dominio

    client_max_body_size 20M;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_redirect off;
        proxy_buffering off;
    }

    location /static {
        alias /var/www/preprocessing/static;
        expires 30d;
        add_header Cache-Control "public, immutable";
    }

    location /uploads {
        alias /var/www/preprocessing/uploads;
        internal;
    }
}
```

```bash
# Habilitar sitio
sudo ln -s /etc/nginx/sites-available/preprocessing /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

### Configuración de SSL (HTTPS)

```bash
# Instalar Certbot
sudo apt install certbot python3-certbot-nginx -y

# Obtener certificado SSL
sudo certbot --nginx -d tu_dominio.com

# Renovación automática (ya configurada por certbot)
sudo certbot renew --dry-run
```

## 3. Despliegue en Heroku

### Requisitos
- Cuenta de Heroku
- Heroku CLI instalado
- Git

### Archivos Necesarios

**Procfile:**
```bash
echo "web: gunicorn run:app" > Procfile
```

**runtime.txt:**
```bash
echo "python-3.9.16" > runtime.txt
```

**requirements.txt** (ya existe, verificar que incluya):
```
gunicorn
psycopg2-binary
```

### Pasos de Despliegue

```bash
# 1. Login en Heroku
heroku login

# 2. Crear aplicación
heroku create nombre-de-tu-app

# 3. Agregar PostgreSQL
heroku addons:create heroku-postgresql:hobby-dev

# 4. Configurar variables de entorno
heroku config:set FLASK_ENV=production
heroku config:set SECRET_KEY=$(python -c 'import secrets; print(secrets.token_hex(32))')

# 5. Desplegar
git push heroku main

# 6. Inicializar base de datos
heroku run flask db upgrade

# 7. Descargar datasets (opcional, puede tardar)
heroku run python download_datasets.py

# 8. Abrir aplicación
heroku open

# Ver logs
heroku logs --tail
```

### Configuración Adicional para Heroku

Modificar `config.py` para usar DATABASE_URL de Heroku:

```python
import os

class Config:
    # ... otras configuraciones ...
    
    # Para Heroku
    DATABASE_URL = os.environ.get('DATABASE_URL')
    if DATABASE_URL and DATABASE_URL.startswith('postgres://'):
        DATABASE_URL = DATABASE_URL.replace('postgres://', 'postgresql://', 1)
    
    SQLALCHEMY_DATABASE_URI = DATABASE_URL or \
        'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'app.db')
```

## Mantenimiento

### Backup de Base de Datos

**PostgreSQL:**
```bash
# Backup
pg_dump -U preprocessing_user preprocessing_db > backup_$(date +%Y%m%d).sql

# Restaurar
psql -U preprocessing_user preprocessing_db < backup_20240101.sql
```

**SQLite (desarrollo):**
```bash
# Backup
cp instance/app.db instance/app_backup_$(date +%Y%m%d).db
```

### Actualización de la Aplicación

```bash
# En el servidor
cd /var/www/preprocessing
git pull origin main
source venv/bin/activate
pip install -r requirements.txt
flask db upgrade
sudo supervisorctl restart preprocessing
```

### Monitoreo

**Ver logs en tiempo real:**
```bash
# Gunicorn
tail -f /var/www/preprocessing/logs/gunicorn_error.log

# Nginx
sudo tail -f /var/nginx/error.log

# Supervisor
sudo tail -f /var/www/preprocessing/logs/supervisor_error.log
```

**Verificar estado:**
```bash
# Supervisor
sudo supervisorctl status preprocessing

# Nginx
sudo systemctl status nginx

# PostgreSQL
sudo systemctl status postgresql
```

## Seguridad

### Mejores Prácticas

1. **Firewall:**
```bash
sudo ufw allow 22/tcp
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw enable
```

2. **Actualizar SECRET_KEY:**
```python
# Generar clave segura
python -c 'import secrets; print(secrets.token_hex(32))'
```

3. **Limitar tamaño de uploads:**
```python
# En config.py
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB
```

4. **Configurar CORS apropiadamente:**
```python
# Solo permitir tu dominio
CORS(app, resources={r"/api/*": {"origins": "https://tu-dominio.com"}})
```

5. **Usar HTTPS siempre en producción**

6. **Backups automáticos:**
```bash
# Agregar a crontab
crontab -e

# Backup diario a las 2 AM
0 2 * * * pg_dump -U preprocessing_user preprocessing_db > /backups/db_$(date +\%Y\%m\%d).sql
```

## Troubleshooting

### Problema: Aplicación no inicia

**Solución:**
```bash
# Verificar logs
sudo supervisorctl tail -f preprocessing stderr

# Verificar permisos
ls -la /var/www/preprocessing

# Verificar entorno virtual
source venv/bin/activate
python -c "import flask; print(flask.__version__)"
```

### Problema: Error 502 Bad Gateway

**Solución:**
```bash
# Verificar que Gunicorn esté corriendo
sudo supervisorctl status preprocessing

# Reiniciar servicios
sudo supervisorctl restart preprocessing
sudo systemctl restart nginx
```

### Problema: Base de datos no conecta

**Solución:**
```bash
# Verificar PostgreSQL
sudo systemctl status postgresql

# Verificar credenciales en .env
cat .env | grep DATABASE_URL

# Probar conexión
psql -U preprocessing_user -d preprocessing_db -h localhost
```

### Problema: Archivos no se suben

**Solución:**
```bash
# Verificar permisos
sudo chown -R www-data:www-data /var/www/preprocessing/uploads
sudo chmod -R 755 /var/www/preprocessing/uploads

# Verificar tamaño máximo en Nginx
sudo nano /etc/nginx/sites-available/preprocessing
# Agregar: client_max_body_size 20M;
```

## Escalabilidad

### Para mayor tráfico:

1. **Aumentar workers de Gunicorn:**
```python
# gunicorn_config.py
workers = (2 * num_cores) + 1
```

2. **Usar Redis para sesiones:**
```bash
pip install redis flask-session
```

3. **CDN para archivos estáticos:**
- Usar AWS S3 + CloudFront
- O Cloudflare

4. **Load Balancer:**
- Nginx como load balancer
- Múltiples instancias de la aplicación

## Recursos Adicionales

- [Flask Deployment](https://flask.palletsprojects.com/en/2.3.x/deploying/)
- [Gunicorn Documentation](https://docs.gunicorn.org/)
- [Nginx Documentation](https://nginx.org/en/docs/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)

---

=======
# Guía de Despliegue - Plataforma de Preprocesamiento

## 📋 Opciones de Despliegue

Esta guía cubre tres opciones de despliegue:
1. **Desarrollo Local** (para pruebas)
2. **Servidor Linux** (producción)
3. **Heroku** (cloud hosting)

## 1. Despliegue Local (Desarrollo)

### Requisitos
- Python 3.8+
- Git
- 2GB RAM mínimo

### Pasos

```bash
# 1. Clonar repositorio
git clone <repository-url>
cd Preprocesamiento

# 2. Crear entorno virtual
python -m venv venv

# Windows
.\venv\Scripts\activate

# Linux/Mac
source venv/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Configurar variables de entorno
cp .env.example .env
# Editar .env con tus configuraciones

# 5. Descargar datasets
python download_datasets.py

# 6. Inicializar base de datos
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

# 7. Ejecutar aplicación
python run.py
```

Accede a: `http://localhost:5000`

## 2. Despliegue en Servidor Linux

### Requisitos
- Ubuntu 20.04+ o similar
- Python 3.8+
- Nginx
- Supervisor (para gestión de procesos)
- PostgreSQL (recomendado para producción)

### Instalación de Dependencias

```bash
# Actualizar sistema
sudo apt update && sudo apt upgrade -y

# Instalar Python y herramientas
sudo apt install python3-pip python3-venv nginx supervisor postgresql postgresql-contrib -y

# Instalar dependencias del sistema para pandas/numpy
sudo apt install python3-dev libpq-dev build-essential -y
```

### Configuración de PostgreSQL

```bash
# Crear usuario y base de datos
sudo -u postgres psql

CREATE DATABASE preprocessing_db;
CREATE USER preprocessing_user WITH PASSWORD 'tu_contraseña_segura';
GRANT ALL PRIVILEGES ON DATABASE preprocessing_db TO preprocessing_user;
\q
```

### Configuración de la Aplicación

```bash
# Crear directorio de aplicación
sudo mkdir -p /var/www/preprocessing
sudo chown $USER:$USER /var/www/preprocessing

# Clonar repositorio
cd /var/www/preprocessing
git clone <repository-url> .

# Crear entorno virtual
python3 -m venv venv
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
pip install gunicorn psycopg2-binary

# Configurar variables de entorno
nano .env
```

**Contenido de .env para producción:**
```env
FLASK_APP=run.py
FLASK_ENV=production
SECRET_KEY=tu_clave_secreta_muy_larga_y_aleatoria
DATABASE_URL=postgresql://preprocessing_user:tu_contraseña_segura@localhost/preprocessing_db
UPLOAD_FOLDER=/var/www/preprocessing/uploads
DATASET_FOLDER=/var/www/preprocessing/datasets
MAX_CONTENT_LENGTH=16777216
```

```bash
# Descargar datasets
python download_datasets.py

# Inicializar base de datos
flask db upgrade

# Crear directorios necesarios
mkdir -p uploads datasets static/uploads
chmod 755 uploads datasets static/uploads
```

### Configuración de Gunicorn

Crear archivo de configuración:
```bash
nano gunicorn_config.py
```

```python
# gunicorn_config.py
bind = "127.0.0.1:8000"
workers = 4
worker_class = "sync"
worker_connections = 1000
timeout = 120
keepalive = 5
errorlog = "/var/www/preprocessing/logs/gunicorn_error.log"
accesslog = "/var/www/preprocessing/logs/gunicorn_access.log"
loglevel = "info"
```

```bash
# Crear directorio de logs
mkdir -p logs
```

### Configuración de Supervisor

```bash
sudo nano /etc/supervisor/conf.d/preprocessing.conf
```

```ini
[program:preprocessing]
directory=/var/www/preprocessing
command=/var/www/preprocessing/venv/bin/gunicorn -c gunicorn_config.py run:app
user=www-data
autostart=true
autorestart=true
stopasgroup=true
killasgroup=true
stderr_logfile=/var/www/preprocessing/logs/supervisor_error.log
stdout_logfile=/var/www/preprocessing/logs/supervisor_output.log
```

```bash
# Actualizar supervisor
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl start preprocessing
sudo supervisorctl status preprocessing
```

### Configuración de Nginx

```bash
sudo nano /etc/nginx/sites-available/preprocessing
```

```nginx
server {
    listen 80;
    server_name tu_dominio.com;  # Cambiar por tu dominio

    client_max_body_size 20M;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_redirect off;
        proxy_buffering off;
    }

    location /static {
        alias /var/www/preprocessing/static;
        expires 30d;
        add_header Cache-Control "public, immutable";
    }

    location /uploads {
        alias /var/www/preprocessing/uploads;
        internal;
    }
}
```

```bash
# Habilitar sitio
sudo ln -s /etc/nginx/sites-available/preprocessing /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

### Configuración de SSL (HTTPS)

```bash
# Instalar Certbot
sudo apt install certbot python3-certbot-nginx -y

# Obtener certificado SSL
sudo certbot --nginx -d tu_dominio.com

# Renovación automática (ya configurada por certbot)
sudo certbot renew --dry-run
```

## 3. Despliegue en Heroku

### Requisitos
- Cuenta de Heroku
- Heroku CLI instalado
- Git

### Archivos Necesarios

**Procfile:**
```bash
echo "web: gunicorn run:app" > Procfile
```

**runtime.txt:**
```bash
echo "python-3.9.16" > runtime.txt
```

**requirements.txt** (ya existe, verificar que incluya):
```
gunicorn
psycopg2-binary
```

### Pasos de Despliegue

```bash
# 1. Login en Heroku
heroku login

# 2. Crear aplicación
heroku create nombre-de-tu-app

# 3. Agregar PostgreSQL
heroku addons:create heroku-postgresql:hobby-dev

# 4. Configurar variables de entorno
heroku config:set FLASK_ENV=production
heroku config:set SECRET_KEY=$(python -c 'import secrets; print(secrets.token_hex(32))')

# 5. Desplegar
git push heroku main

# 6. Inicializar base de datos
heroku run flask db upgrade

# 7. Descargar datasets (opcional, puede tardar)
heroku run python download_datasets.py

# 8. Abrir aplicación
heroku open

# Ver logs
heroku logs --tail
```

### Configuración Adicional para Heroku

Modificar `config.py` para usar DATABASE_URL de Heroku:

```python
import os

class Config:
    # ... otras configuraciones ...
    
    # Para Heroku
    DATABASE_URL = os.environ.get('DATABASE_URL')
    if DATABASE_URL and DATABASE_URL.startswith('postgres://'):
        DATABASE_URL = DATABASE_URL.replace('postgres://', 'postgresql://', 1)
    
    SQLALCHEMY_DATABASE_URI = DATABASE_URL or \
        'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'app.db')
```

## Mantenimiento

### Backup de Base de Datos

**PostgreSQL:**
```bash
# Backup
pg_dump -U preprocessing_user preprocessing_db > backup_$(date +%Y%m%d).sql

# Restaurar
psql -U preprocessing_user preprocessing_db < backup_20240101.sql
```

**SQLite (desarrollo):**
```bash
# Backup
cp instance/app.db instance/app_backup_$(date +%Y%m%d).db
```

### Actualización de la Aplicación

```bash
# En el servidor
cd /var/www/preprocessing
git pull origin main
source venv/bin/activate
pip install -r requirements.txt
flask db upgrade
sudo supervisorctl restart preprocessing
```

### Monitoreo

**Ver logs en tiempo real:**
```bash
# Gunicorn
tail -f /var/www/preprocessing/logs/gunicorn_error.log

# Nginx
sudo tail -f /var/nginx/error.log

# Supervisor
sudo tail -f /var/www/preprocessing/logs/supervisor_error.log
```

**Verificar estado:**
```bash
# Supervisor
sudo supervisorctl status preprocessing

# Nginx
sudo systemctl status nginx

# PostgreSQL
sudo systemctl status postgresql
```

## Seguridad

### Mejores Prácticas

1. **Firewall:**
```bash
sudo ufw allow 22/tcp
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw enable
```

2. **Actualizar SECRET_KEY:**
```python
# Generar clave segura
python -c 'import secrets; print(secrets.token_hex(32))'
```

3. **Limitar tamaño de uploads:**
```python
# En config.py
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB
```

4. **Configurar CORS apropiadamente:**
```python
# Solo permitir tu dominio
CORS(app, resources={r"/api/*": {"origins": "https://tu-dominio.com"}})
```

5. **Usar HTTPS siempre en producción**

6. **Backups automáticos:**
```bash
# Agregar a crontab
crontab -e

# Backup diario a las 2 AM
0 2 * * * pg_dump -U preprocessing_user preprocessing_db > /backups/db_$(date +\%Y\%m\%d).sql
```

## Troubleshooting

### Problema: Aplicación no inicia

**Solución:**
```bash
# Verificar logs
sudo supervisorctl tail -f preprocessing stderr

# Verificar permisos
ls -la /var/www/preprocessing

# Verificar entorno virtual
source venv/bin/activate
python -c "import flask; print(flask.__version__)"
```

### Problema: Error 502 Bad Gateway

**Solución:**
```bash
# Verificar que Gunicorn esté corriendo
sudo supervisorctl status preprocessing

# Reiniciar servicios
sudo supervisorctl restart preprocessing
sudo systemctl restart nginx
```

### Problema: Base de datos no conecta

**Solución:**
```bash
# Verificar PostgreSQL
sudo systemctl status postgresql

# Verificar credenciales en .env
cat .env | grep DATABASE_URL

# Probar conexión
psql -U preprocessing_user -d preprocessing_db -h localhost
```

### Problema: Archivos no se suben

**Solución:**
```bash
# Verificar permisos
sudo chown -R www-data:www-data /var/www/preprocessing/uploads
sudo chmod -R 755 /var/www/preprocessing/uploads

# Verificar tamaño máximo en Nginx
sudo nano /etc/nginx/sites-available/preprocessing
# Agregar: client_max_body_size 20M;
```

## Escalabilidad

### Para mayor tráfico:

1. **Aumentar workers de Gunicorn:**
```python
# gunicorn_config.py
workers = (2 * num_cores) + 1
```

2. **Usar Redis para sesiones:**
```bash
pip install redis flask-session
```

3. **CDN para archivos estáticos:**
- Usar AWS S3 + CloudFront
- O Cloudflare

4. **Load Balancer:**
- Nginx como load balancer
- Múltiples instancias de la aplicación

## Recursos Adicionales

- [Flask Deployment](https://flask.palletsprojects.com/en/2.3.x/deploying/)
- [Gunicorn Documentation](https://docs.gunicorn.org/)
- [Nginx Documentation](https://nginx.org/en/docs/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)

---

>>>>>>> 5cacc14741e04989bfeb01a4c6f9a705353a88f4
**¡Aplicación lista para producción! 🚀**