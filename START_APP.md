<<<<<<< HEAD
# 🚀 Cómo Iniciar la Aplicación

## Pasos para Ejecutar por Primera Vez

### 1. Verificar que las dependencias estén instaladas
```bash
.\venv\Scripts\python.exe -m pip list
```

Deberías ver Flask, pandas, scikit-learn, etc.

### 2. Descargar los datasets de ejemplo
```bash
.\venv\Scripts\python.exe download_datasets.py
```

Esto creará 4 datasets en `static/datasets/`:
- iris.csv
- wine.csv
- breast_cancer.csv
- sample_data.csv (con valores faltantes y outliers)

### 3. Inicializar la base de datos
```bash
.\venv\Scripts\python.exe -c "from app import create_app, db; app = create_app(); app.app_context().push(); db.create_all(); print('Database created!')"
```

### 4. Ejecutar la aplicación
```bash
.\venv\Scripts\python.exe run.py
```

### 5. Abrir en el navegador
Abre tu navegador y ve a: **http://localhost:5000**

---

## 🎯 Primera Vez Usando la Aplicación

### Paso 1: Registrarse
1. Haz clic en "Registrarse" en la página principal
2. Completa el formulario con:
   - Usuario
   - Email
   - Contraseña (mínimo 6 caracteres)
3. Haz clic en "Registrarse"

### Paso 2: Iniciar Sesión
1. Usa tus credenciales para iniciar sesión
2. Serás redirigido al Dashboard

### Paso 3: Explorar la Plataforma

#### 📚 Teoría
- Ve a "Teoría" en el menú
- Explora los 4 módulos:
  - Limpieza de Datos
  - Transformación de Datos
  - Integración de Datos
  - Reducción de Dimensionalidad

#### 🔬 Laboratorio de Práctica
- Ve a "Práctica" en el menú
- Selecciona un dataset pre-cargado o sube el tuyo
- Aplica operaciones de preprocesamiento
- Visualiza los resultados

#### 📊 Dashboard
- Revisa tu progreso
- Ve tus estadísticas
- Accede a pipelines guardados

---

## 🛠️ Comandos Útiles

### Detener la aplicación
Presiona `Ctrl + C` en la terminal

### Reiniciar la aplicación
```bash
.\venv\Scripts\python.exe run.py
```

### Ver logs
Los logs aparecen en la terminal donde ejecutaste `run.py`

### Limpiar base de datos
```bash
Remove-Item data-dev.db
.\venv\Scripts\python.exe -c "from app import create_app, db; app = create_app(); app.app_context().push(); db.create_all(); print('Database reset!')"
```

### Crear usuario admin
```bash
.\venv\Scripts\python.exe run.py create_admin
```

---

## 📝 Estructura de URLs

- **Inicio:** http://localhost:5000/
- **Login:** http://localhost:5000/auth/login
- **Registro:** http://localhost:5000/auth/register
- **Dashboard:** http://localhost:5000/dashboard
- **Teoría:** http://localhost:5000/theory
- **Práctica:** http://localhost:5000/practice
- **Quizzes:** http://localhost:5000/quiz
- **Progreso:** http://localhost:5000/progress
- **API:** http://localhost:5000/api/*

---

## 🐛 Solución de Problemas

### Error: "Address already in use"
El puerto 5000 está ocupado. Cambia el puerto en `run.py`:
```python
app.run(debug=True, host='0.0.0.0', port=5001)
```

### Error: "No module named 'flask'"
Las dependencias no están instaladas. Ejecuta:
```bash
.\venv\Scripts\python.exe -m pip install -r requirements.txt
```

### Error: "Database not found"
Inicializa la base de datos con el comando del paso 3.

### La página no carga
1. Verifica que la aplicación esté corriendo
2. Revisa la terminal por errores
3. Intenta acceder a http://127.0.0.1:5000

### Errores de importación
Asegúrate de estar usando el Python del venv:
```bash
.\venv\Scripts\python.exe run.py
```

---

## 🎨 Personalización

### Cambiar el puerto
Edita `run.py` línea 56:
```python
app.run(debug=True, host='0.0.0.0', port=TU_PUERTO)
```

### Cambiar colores
Edita `static/css/main.css` y modifica las variables CSS en `:root`

### Agregar más datasets
Coloca archivos CSV en `static/datasets/`

---

## 📚 Próximos Pasos de Desarrollo

1. **Completar contenido de teoría** (2-3 horas)
   - Expandir las páginas de teoría con más contenido
   - Agregar ejemplos de código
   - Incluir diagramas

2. **Implementar quizzes completos** (1-2 horas)
   - Crear banco de preguntas en JSON
   - Implementar lógica de calificación
   - Agregar retroalimentación

3. **Mejorar laboratorio** (2-3 horas)
   - Hacer interfaz más interactiva
   - Agregar más operaciones
   - Implementar preview en tiempo real

4. **Testing** (1 hora)
   - Probar todas las funcionalidades
   - Corregir bugs
   - Optimizar rendimiento

---

## ✅ Checklist de Verificación

Antes de considerar el proyecto completo, verifica:

- [ ] La aplicación inicia sin errores
- [ ] Puedes registrarte e iniciar sesión
- [ ] El dashboard muestra información
- [ ] Puedes acceder a todas las páginas
- [ ] Los datasets se cargan correctamente
- [ ] Las visualizaciones funcionan
- [ ] El CSS se aplica correctamente
- [ ] No hay errores en la consola del navegador

---

## 🎉 ¡Listo!

Si todo funciona correctamente, ¡felicidades! Tienes una plataforma educativa funcional para enseñar preprocesamiento de datos.

=======
# 🚀 Cómo Iniciar la Aplicación

## Pasos para Ejecutar por Primera Vez

### 1. Verificar que las dependencias estén instaladas
```bash
.\venv\Scripts\python.exe -m pip list
```

Deberías ver Flask, pandas, scikit-learn, etc.

### 2. Descargar los datasets de ejemplo
```bash
.\venv\Scripts\python.exe download_datasets.py
```

Esto creará 4 datasets en `static/datasets/`:
- iris.csv
- wine.csv
- breast_cancer.csv
- sample_data.csv (con valores faltantes y outliers)

### 3. Inicializar la base de datos
```bash
.\venv\Scripts\python.exe -c "from app import create_app, db; app = create_app(); app.app_context().push(); db.create_all(); print('Database created!')"
```

### 4. Ejecutar la aplicación
```bash
.\venv\Scripts\python.exe run.py
```

### 5. Abrir en el navegador
Abre tu navegador y ve a: **http://localhost:5000**

---

## 🎯 Primera Vez Usando la Aplicación

### Paso 1: Registrarse
1. Haz clic en "Registrarse" en la página principal
2. Completa el formulario con:
   - Usuario
   - Email
   - Contraseña (mínimo 6 caracteres)
3. Haz clic en "Registrarse"

### Paso 2: Iniciar Sesión
1. Usa tus credenciales para iniciar sesión
2. Serás redirigido al Dashboard

### Paso 3: Explorar la Plataforma

#### 📚 Teoría
- Ve a "Teoría" en el menú
- Explora los 4 módulos:
  - Limpieza de Datos
  - Transformación de Datos
  - Integración de Datos
  - Reducción de Dimensionalidad

#### 🔬 Laboratorio de Práctica
- Ve a "Práctica" en el menú
- Selecciona un dataset pre-cargado o sube el tuyo
- Aplica operaciones de preprocesamiento
- Visualiza los resultados

#### 📊 Dashboard
- Revisa tu progreso
- Ve tus estadísticas
- Accede a pipelines guardados

---

## 🛠️ Comandos Útiles

### Detener la aplicación
Presiona `Ctrl + C` en la terminal

### Reiniciar la aplicación
```bash
.\venv\Scripts\python.exe run.py
```

### Ver logs
Los logs aparecen en la terminal donde ejecutaste `run.py`

### Limpiar base de datos
```bash
Remove-Item data-dev.db
.\venv\Scripts\python.exe -c "from app import create_app, db; app = create_app(); app.app_context().push(); db.create_all(); print('Database reset!')"
```

### Crear usuario admin
```bash
.\venv\Scripts\python.exe run.py create_admin
```

---

## 📝 Estructura de URLs

- **Inicio:** http://localhost:5000/
- **Login:** http://localhost:5000/auth/login
- **Registro:** http://localhost:5000/auth/register
- **Dashboard:** http://localhost:5000/dashboard
- **Teoría:** http://localhost:5000/theory
- **Práctica:** http://localhost:5000/practice
- **Quizzes:** http://localhost:5000/quiz
- **Progreso:** http://localhost:5000/progress
- **API:** http://localhost:5000/api/*

---

## 🐛 Solución de Problemas

### Error: "Address already in use"
El puerto 5000 está ocupado. Cambia el puerto en `run.py`:
```python
app.run(debug=True, host='0.0.0.0', port=5001)
```

### Error: "No module named 'flask'"
Las dependencias no están instaladas. Ejecuta:
```bash
.\venv\Scripts\python.exe -m pip install -r requirements.txt
```

### Error: "Database not found"
Inicializa la base de datos con el comando del paso 3.

### La página no carga
1. Verifica que la aplicación esté corriendo
2. Revisa la terminal por errores
3. Intenta acceder a http://127.0.0.1:5000

### Errores de importación
Asegúrate de estar usando el Python del venv:
```bash
.\venv\Scripts\python.exe run.py
```

---

## 🎨 Personalización

### Cambiar el puerto
Edita `run.py` línea 56:
```python
app.run(debug=True, host='0.0.0.0', port=TU_PUERTO)
```

### Cambiar colores
Edita `static/css/main.css` y modifica las variables CSS en `:root`

### Agregar más datasets
Coloca archivos CSV en `static/datasets/`

---

## 📚 Próximos Pasos de Desarrollo

1. **Completar contenido de teoría** (2-3 horas)
   - Expandir las páginas de teoría con más contenido
   - Agregar ejemplos de código
   - Incluir diagramas

2. **Implementar quizzes completos** (1-2 horas)
   - Crear banco de preguntas en JSON
   - Implementar lógica de calificación
   - Agregar retroalimentación

3. **Mejorar laboratorio** (2-3 horas)
   - Hacer interfaz más interactiva
   - Agregar más operaciones
   - Implementar preview en tiempo real

4. **Testing** (1 hora)
   - Probar todas las funcionalidades
   - Corregir bugs
   - Optimizar rendimiento

---

## ✅ Checklist de Verificación

Antes de considerar el proyecto completo, verifica:

- [ ] La aplicación inicia sin errores
- [ ] Puedes registrarte e iniciar sesión
- [ ] El dashboard muestra información
- [ ] Puedes acceder a todas las páginas
- [ ] Los datasets se cargan correctamente
- [ ] Las visualizaciones funcionan
- [ ] El CSS se aplica correctamente
- [ ] No hay errores en la consola del navegador

---

## 🎉 ¡Listo!

Si todo funciona correctamente, ¡felicidades! Tienes una plataforma educativa funcional para enseñar preprocesamiento de datos.

>>>>>>> 5cacc14741e04989bfeb01a4c6f9a705353a88f4
**Disfruta explorando y aprendiendo!** 🚀