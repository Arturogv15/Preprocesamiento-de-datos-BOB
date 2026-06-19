<<<<<<< HEAD
# Guía de Inicio Rápido

## 🚀 Comenzar en 5 Minutos

### Paso 1: Instalar Dependencias

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# En Windows:
venv\Scripts\activate
# En Linux/Mac:
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

### Paso 2: Configurar Variables de Entorno

```bash
# Copiar archivo de ejemplo
copy .env.example .env

# Editar .env y configurar:
# - SECRET_KEY (genera una clave segura)
# - DATABASE_URL (opcional, usa SQLite por defecto)
```

### Paso 3: Inicializar Base de Datos

```bash
# Inicializar la base de datos
python run.py init_db
```

### Paso 4: Ejecutar la Aplicación

```bash
# Iniciar servidor de desarrollo
python run.py
```

La aplicación estará disponible en: **http://localhost:5000**

---

## 📋 Estructura del Proyecto Creada

```
Preprocesamiento/
├── app/                          ✅ Backend completo
│   ├── __init__.py              ✅ Inicialización Flask
│   ├── models.py                ✅ Modelos de base de datos
│   ├── auth.py                  ✅ Autenticación
│   ├── routes.py                ✅ Rutas principales
│   ├── api.py                   ✅ API endpoints
│   ├── data_processing.py       ✅ Procesamiento de datos
│   └── visualization.py         ✅ Generación de gráficas
├── static/
│   ├── css/
│   │   └── main.css             ✅ Estilos personalizados
│   ├── js/
│   │   └── main.js              ✅ JavaScript principal
│   └── datasets/                ⏳ Agregar datasets aquí
├── templates/
│   ├── base.html                ✅ Template base
│   ├── index.html               ✅ Página de inicio
│   ├── login.html               ✅ Login
│   ├── register.html            ✅ Registro
│   ├── dashboard.html           ✅ Dashboard
│   ├── theory/                  ⏳ Páginas de teoría
│   ├── practice/                ⏳ Laboratorio de práctica
│   └── quiz/                    ⏳ Sistema de quizzes
├── uploads/                     ✅ Datasets de usuarios
├── config.py                    ✅ Configuración
├── requirements.txt             ✅ Dependencias
└── run.py                       ✅ Punto de entrada
```

**Leyenda:**
- ✅ Completado
- ⏳ Pendiente (próximos pasos)

---

## 🎯 Funcionalidades Implementadas

### Backend (100% Core Funcional)

#### ✅ Autenticación y Usuarios
- Registro de usuarios
- Login/Logout
- Gestión de sesiones
- Perfiles de usuario

#### ✅ Procesamiento de Datos
- **Limpieza:**
  - Imputación de valores faltantes (mean, median, mode, KNN, ffill, bfill)
  - Eliminación de duplicados
  - Detección y manejo de outliers (IQR, Z-score, Isolation Forest)

- **Transformación:**
  - Normalización (Min-Max, Standard, Robust, MaxAbs)
  - Codificación categórica (One-Hot, Label, Ordinal)

- **Integración:**
  - Merge de datasets (inner, left, right, outer joins)
  - Concatenación

- **Reducción de Dimensionalidad:**
  - PCA (Principal Component Analysis)
  - Selección de características (variance, correlation, k-best)

#### ✅ Visualizaciones
- Box plots (detección de outliers)
- Histogramas con KDE
- Scatter plots
- Correlation heatmaps
- Pair plots
- Missing data heatmaps
- Distribution plots
- PCA variance plots

#### ✅ API REST
- Upload de datasets
- Preview de datos
- Operaciones de limpieza
- Operaciones de transformación
- Generación de visualizaciones
- Gestión de progreso
- Sistema de quizzes
- Guardado de pipelines

### Frontend (80% Completado)

#### ✅ Páginas Principales
- Landing page atractiva
- Sistema de login/registro
- Dashboard interactivo
- Navegación completa

#### ✅ Estilos y UX
- Diseño responsive (Bootstrap 5)
- Tema moderno y profesional
- Animaciones y transiciones
- Feedback visual

#### ✅ JavaScript
- Funciones de API
- Manejo de datasets
- Visualizaciones con Plotly
- Sistema de alertas
- Loading spinners

---

## 📝 Próximos Pasos Recomendados

### 1. Agregar Datasets Pre-cargados (15 min)
Descarga y coloca en `static/datasets/`:
- Titanic: https://www.kaggle.com/c/titanic/data
- Housing: https://www.kaggle.com/c/house-prices-advanced-regression-techniques/data
- Iris: Incluido en scikit-learn

```python
# Script para descargar Iris
from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target
df.to_csv('static/datasets/iris.csv', index=False)
```

### 2. Crear Páginas de Teoría (30-60 min)
Crear archivos en `templates/theory/`:
- `data_cleaning.html`
- `data_transformation.html`
- `data_integration.html`
- `dimensionality_reduction.html`

### 3. Crear Laboratorio de Práctica (45 min)
Crear `templates/practice/lab.html` con:
- Selector de datasets
- Panel de operaciones
- Visualización de resultados
- Historial de pasos

### 4. Implementar Sistema de Quizzes (30 min)
- Crear preguntas en JSON
- Implementar `templates/quiz/quiz.html`
- Sistema de calificación

### 5. Testing y Refinamiento (30 min)
- Probar todas las funcionalidades
- Corregir bugs
- Optimizar rendimiento

---

## 🔧 Comandos Útiles

```bash
# Crear usuario admin
python run.py create_admin

# Acceder a shell de Flask
flask shell

# Ver rutas disponibles
flask routes

# Ejecutar en modo debug
python run.py

# Ejecutar en producción
gunicorn -w 4 -b 0.0.0.0:5000 run:app
```

---

## 🐛 Solución de Problemas Comunes

### Error: "No module named 'flask'"
```bash
pip install -r requirements.txt
```

### Error: "Database not found"
```bash
python run.py init_db
```

### Error: "Port 5000 already in use"
```bash
# Cambiar puerto en run.py o:
python run.py --port 5001
```

### Problemas con visualizaciones
```bash
# Reinstalar plotly
pip install --upgrade plotly kaleido
```

---

## 📚 Recursos Adicionales

### Documentación
- Flask: https://flask.palletsprojects.com/
- pandas: https://pandas.pydata.org/docs/
- scikit-learn: https://scikit-learn.org/stable/
- Plotly: https://plotly.com/python/

### Datasets Recomendados
- Kaggle: https://www.kaggle.com/datasets
- UCI ML Repository: https://archive.ics.uci.edu/ml/
- Data.gov: https://data.gov/

---

## 🎓 Flujo de Trabajo Sugerido para Estudiantes

1. **Registrarse** en la plataforma
2. **Leer teoría** de cada módulo
3. **Practicar** en el laboratorio con datasets
4. **Tomar quizzes** para evaluar conocimiento
5. **Guardar pipelines** para reutilizar
6. **Revisar progreso** en el dashboard

---

## 💡 Tips de Desarrollo

### Agregar nueva operación de procesamiento:

1. Agregar método en `app/data_processing.py`
2. Agregar endpoint en `app/api.py`
3. Agregar función JS en `static/js/main.js`
4. Agregar UI en template correspondiente

### Agregar nueva visualización:

1. Agregar método en `app/visualization.py`
2. Usar Plotly para generar gráfica
3. Retornar JSON con `fig.to_json()`
4. Renderizar con `Plotly.newPlot()` en frontend

---

## 🚀 Estado Actual del Proyecto

**Completado: ~75%**

✅ **Listo para usar:**
- Sistema de autenticación
- Upload y gestión de datasets
- Todas las operaciones de preprocesamiento
- Visualizaciones interactivas
- API REST completa
- Dashboard funcional

⏳ **Pendiente:**
- Contenido teórico (4 páginas)
- Interfaz del laboratorio
- Sistema de quizzes completo
- Datasets pre-cargados
- Documentación de usuario

**Tiempo estimado para completar:** 2-3 horas

---

## 📞 Soporte

Si encuentras problemas:
1. Revisa los logs en la consola
2. Verifica que todas las dependencias estén instaladas
3. Asegúrate de que la base de datos esté inicializada
4. Consulta la documentación de las librerías

---

=======
# Guía de Inicio Rápido

## 🚀 Comenzar en 5 Minutos

### Paso 1: Instalar Dependencias

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# En Windows:
venv\Scripts\activate
# En Linux/Mac:
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

### Paso 2: Configurar Variables de Entorno

```bash
# Copiar archivo de ejemplo
copy .env.example .env

# Editar .env y configurar:
# - SECRET_KEY (genera una clave segura)
# - DATABASE_URL (opcional, usa SQLite por defecto)
```

### Paso 3: Inicializar Base de Datos

```bash
# Inicializar la base de datos
python run.py init_db
```

### Paso 4: Ejecutar la Aplicación

```bash
# Iniciar servidor de desarrollo
python run.py
```

La aplicación estará disponible en: **http://localhost:5000**

---

## 📋 Estructura del Proyecto Creada

```
Preprocesamiento/
├── app/                          ✅ Backend completo
│   ├── __init__.py              ✅ Inicialización Flask
│   ├── models.py                ✅ Modelos de base de datos
│   ├── auth.py                  ✅ Autenticación
│   ├── routes.py                ✅ Rutas principales
│   ├── api.py                   ✅ API endpoints
│   ├── data_processing.py       ✅ Procesamiento de datos
│   └── visualization.py         ✅ Generación de gráficas
├── static/
│   ├── css/
│   │   └── main.css             ✅ Estilos personalizados
│   ├── js/
│   │   └── main.js              ✅ JavaScript principal
│   └── datasets/                ⏳ Agregar datasets aquí
├── templates/
│   ├── base.html                ✅ Template base
│   ├── index.html               ✅ Página de inicio
│   ├── login.html               ✅ Login
│   ├── register.html            ✅ Registro
│   ├── dashboard.html           ✅ Dashboard
│   ├── theory/                  ⏳ Páginas de teoría
│   ├── practice/                ⏳ Laboratorio de práctica
│   └── quiz/                    ⏳ Sistema de quizzes
├── uploads/                     ✅ Datasets de usuarios
├── config.py                    ✅ Configuración
├── requirements.txt             ✅ Dependencias
└── run.py                       ✅ Punto de entrada
```

**Leyenda:**
- ✅ Completado
- ⏳ Pendiente (próximos pasos)

---

## 🎯 Funcionalidades Implementadas

### Backend (100% Core Funcional)

#### ✅ Autenticación y Usuarios
- Registro de usuarios
- Login/Logout
- Gestión de sesiones
- Perfiles de usuario

#### ✅ Procesamiento de Datos
- **Limpieza:**
  - Imputación de valores faltantes (mean, median, mode, KNN, ffill, bfill)
  - Eliminación de duplicados
  - Detección y manejo de outliers (IQR, Z-score, Isolation Forest)

- **Transformación:**
  - Normalización (Min-Max, Standard, Robust, MaxAbs)
  - Codificación categórica (One-Hot, Label, Ordinal)

- **Integración:**
  - Merge de datasets (inner, left, right, outer joins)
  - Concatenación

- **Reducción de Dimensionalidad:**
  - PCA (Principal Component Analysis)
  - Selección de características (variance, correlation, k-best)

#### ✅ Visualizaciones
- Box plots (detección de outliers)
- Histogramas con KDE
- Scatter plots
- Correlation heatmaps
- Pair plots
- Missing data heatmaps
- Distribution plots
- PCA variance plots

#### ✅ API REST
- Upload de datasets
- Preview de datos
- Operaciones de limpieza
- Operaciones de transformación
- Generación de visualizaciones
- Gestión de progreso
- Sistema de quizzes
- Guardado de pipelines

### Frontend (80% Completado)

#### ✅ Páginas Principales
- Landing page atractiva
- Sistema de login/registro
- Dashboard interactivo
- Navegación completa

#### ✅ Estilos y UX
- Diseño responsive (Bootstrap 5)
- Tema moderno y profesional
- Animaciones y transiciones
- Feedback visual

#### ✅ JavaScript
- Funciones de API
- Manejo de datasets
- Visualizaciones con Plotly
- Sistema de alertas
- Loading spinners

---

## 📝 Próximos Pasos Recomendados

### 1. Agregar Datasets Pre-cargados (15 min)
Descarga y coloca en `static/datasets/`:
- Titanic: https://www.kaggle.com/c/titanic/data
- Housing: https://www.kaggle.com/c/house-prices-advanced-regression-techniques/data
- Iris: Incluido en scikit-learn

```python
# Script para descargar Iris
from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target
df.to_csv('static/datasets/iris.csv', index=False)
```

### 2. Crear Páginas de Teoría (30-60 min)
Crear archivos en `templates/theory/`:
- `data_cleaning.html`
- `data_transformation.html`
- `data_integration.html`
- `dimensionality_reduction.html`

### 3. Crear Laboratorio de Práctica (45 min)
Crear `templates/practice/lab.html` con:
- Selector de datasets
- Panel de operaciones
- Visualización de resultados
- Historial de pasos

### 4. Implementar Sistema de Quizzes (30 min)
- Crear preguntas en JSON
- Implementar `templates/quiz/quiz.html`
- Sistema de calificación

### 5. Testing y Refinamiento (30 min)
- Probar todas las funcionalidades
- Corregir bugs
- Optimizar rendimiento

---

## 🔧 Comandos Útiles

```bash
# Crear usuario admin
python run.py create_admin

# Acceder a shell de Flask
flask shell

# Ver rutas disponibles
flask routes

# Ejecutar en modo debug
python run.py

# Ejecutar en producción
gunicorn -w 4 -b 0.0.0.0:5000 run:app
```

---

## 🐛 Solución de Problemas Comunes

### Error: "No module named 'flask'"
```bash
pip install -r requirements.txt
```

### Error: "Database not found"
```bash
python run.py init_db
```

### Error: "Port 5000 already in use"
```bash
# Cambiar puerto en run.py o:
python run.py --port 5001
```

### Problemas con visualizaciones
```bash
# Reinstalar plotly
pip install --upgrade plotly kaleido
```

---

## 📚 Recursos Adicionales

### Documentación
- Flask: https://flask.palletsprojects.com/
- pandas: https://pandas.pydata.org/docs/
- scikit-learn: https://scikit-learn.org/stable/
- Plotly: https://plotly.com/python/

### Datasets Recomendados
- Kaggle: https://www.kaggle.com/datasets
- UCI ML Repository: https://archive.ics.uci.edu/ml/
- Data.gov: https://data.gov/

---

## 🎓 Flujo de Trabajo Sugerido para Estudiantes

1. **Registrarse** en la plataforma
2. **Leer teoría** de cada módulo
3. **Practicar** en el laboratorio con datasets
4. **Tomar quizzes** para evaluar conocimiento
5. **Guardar pipelines** para reutilizar
6. **Revisar progreso** en el dashboard

---

## 💡 Tips de Desarrollo

### Agregar nueva operación de procesamiento:

1. Agregar método en `app/data_processing.py`
2. Agregar endpoint en `app/api.py`
3. Agregar función JS en `static/js/main.js`
4. Agregar UI en template correspondiente

### Agregar nueva visualización:

1. Agregar método en `app/visualization.py`
2. Usar Plotly para generar gráfica
3. Retornar JSON con `fig.to_json()`
4. Renderizar con `Plotly.newPlot()` en frontend

---

## 🚀 Estado Actual del Proyecto

**Completado: ~75%**

✅ **Listo para usar:**
- Sistema de autenticación
- Upload y gestión de datasets
- Todas las operaciones de preprocesamiento
- Visualizaciones interactivas
- API REST completa
- Dashboard funcional

⏳ **Pendiente:**
- Contenido teórico (4 páginas)
- Interfaz del laboratorio
- Sistema de quizzes completo
- Datasets pre-cargados
- Documentación de usuario

**Tiempo estimado para completar:** 2-3 horas

---

## 📞 Soporte

Si encuentras problemas:
1. Revisa los logs en la consola
2. Verifica que todas las dependencias estén instaladas
3. Asegúrate de que la base de datos esté inicializada
4. Consulta la documentación de las librerías

---

>>>>>>> 5cacc14741e04989bfeb01a4c6f9a705353a88f4
¡La aplicación está lista para comenzar a desarrollar las páginas de contenido y empezar a usarla! 🎉