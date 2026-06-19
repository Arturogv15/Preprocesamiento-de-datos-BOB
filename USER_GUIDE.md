<<<<<<< HEAD
# Guía de Usuario - Plataforma de Preprocesamiento de Datos

## 📚 Tabla de Contenidos
1. [Introducción](#introducción)
2. [Primeros Pasos](#primeros-pasos)
3. [Módulos de Teoría](#módulos-de-teoría)
4. [Laboratorio Práctico](#laboratorio-práctico)
5. [Quizzes](#quizzes)
6. [Exportación de Datos](#exportación-de-datos)
7. [Consejos y Mejores Prácticas](#consejos-y-mejores-prácticas)

## Introducción

Esta plataforma está diseñada para ayudarte a aprender y practicar técnicas de preprocesamiento de datos en minería de datos. Incluye:

- **Teoría completa** sobre 4 temas principales
- **Laboratorio interactivo** para practicar con datos reales
- **Quizzes** para evaluar tu conocimiento
- **Datasets precargados** para experimentar
- **Visualizaciones** para análisis exploratorio

## Primeros Pasos

### 1. Registro e Inicio de Sesión

1. Accede a la página principal
2. Haz clic en "Registrarse"
3. Completa el formulario con:
   - Nombre de usuario
   - Email
   - Contraseña
4. Inicia sesión con tus credenciales

### 2. Dashboard

Después de iniciar sesión, verás tu dashboard con:
- **Progreso general**: Porcentaje de módulos completados
- **Módulos disponibles**: Teoría y práctica de cada tema
- **Estadísticas**: Tiempo dedicado y quizzes completados

## Módulos de Teoría

### Limpieza de Datos

Aprende sobre:
- **Valores nulos**: Detección y métodos de imputación
- **Duplicados**: Identificación y eliminación
- **Outliers**: Detección con IQR, Z-score e Isolation Forest
- **Mejores prácticas**: Cuándo y cómo aplicar cada técnica

**Navegación:**
1. Dashboard → "Teoría" → "Limpieza de Datos"
2. Lee el contenido completo
3. Toma notas de los conceptos clave
4. Practica con los ejemplos

### Transformación de Datos

Cubre:
- **Normalización**: Min-Max, Standard, Robust, Max Abs
- **Encoding**: One-Hot, Label, Ordinal, Target
- **Cuándo usar cada método**
- **Ventajas y desventajas**

### Integración de Datos

Incluye:
- **Tipos de Joins**: Inner, Left, Right, Outer
- **Merge vs Concat**: Diferencias y casos de uso
- **Validación**: Cómo verificar resultados
- **Problemas comunes**: Duplicados, pérdida de datos

### Reducción de Dimensionalidad

Explica:
- **PCA**: Análisis de Componentes Principales
- **Selección de características**: Filter, Wrapper, Embedded
- **Comparación**: PCA vs Selección
- **Aplicaciones prácticas**

## Laboratorio Práctico

### Cargar Datos

**Opción 1: Datasets Precargados**
1. Ve a "Práctica" → "Laboratorio"
2. Selecciona un dataset del menú desplegable:
   - Iris (clasificación)
   - Titanic (limpieza de datos)
   - Wine (transformación)
   - California Housing (regresión)
   - Customer Data (calidad de datos)
   - Sales Transactions (integración)

**Opción 2: Subir tu Propio Dataset**
1. Haz clic en "Subir Dataset"
2. Selecciona archivo CSV o Excel
3. Espera la confirmación de carga

### Análisis Exploratorio

**Visualizaciones Disponibles:**

1. **Boxplot**: Detectar outliers
   - Selecciona columna numérica
   - Observa valores atípicos

2. **Histogram**: Distribución de datos
   - Elige columna
   - Ajusta número de bins

3. **Scatter Plot**: Relaciones entre variables
   - Selecciona X e Y
   - Opcional: color por categoría

4. **Heatmap**: Correlaciones
   - Muestra relaciones entre todas las variables numéricas
   - Identifica multicolinealidad

5. **Pairplot**: Múltiples relaciones
   - Visualiza todas las combinaciones
   - Útil para exploración inicial

### Operaciones de Limpieza

**Imputación de Valores Nulos:**
```
1. Selecciona columna con valores nulos
2. Elige método:
   - Media (datos numéricos simétricos)
   - Mediana (datos con outliers)
   - Moda (datos categóricos)
   - KNN (considera relaciones)
   - Forward/Backward Fill (series temporales)
3. Aplica y verifica resultados
```

**Eliminación de Duplicados:**
```
1. Haz clic en "Detectar Duplicados"
2. Revisa filas duplicadas
3. Decide: eliminar o mantener
4. Confirma operación
```

**Tratamiento de Outliers:**
```
1. Selecciona método de detección:
   - IQR (robusto, no asume normalidad)
   - Z-score (asume normalidad)
   - Isolation Forest (alta dimensionalidad)
2. Visualiza outliers detectados
3. Decide: eliminar, transformar o mantener
```

### Operaciones de Transformación

**Normalización:**
```
1. Selecciona columnas numéricas
2. Elige método:
   - Min-Max: rango [0,1]
   - Standard: media=0, std=1
   - Robust: usa mediana e IQR
   - Max Abs: rango [-1,1]
3. Aplica y compara distribuciones
```

**Encoding:**
```
1. Selecciona columnas categóricas
2. Elige método:
   - One-Hot: variables nominales
   - Label: variables ordinales
   - Ordinal: con orden específico
   - Target: basado en variable objetivo
3. Verifica nuevas columnas creadas
```

### Integración de Datos

**Joins:**
```
1. Carga dos datasets
2. Selecciona columnas clave
3. Elige tipo de join:
   - Inner: solo coincidencias
   - Left: todas de izquierda
   - Right: todas de derecha
   - Outer: todas de ambas
4. Valida resultado
```

### Reducción de Dimensionalidad

**PCA:**
```
1. Selecciona características numéricas
2. Estandariza datos (importante!)
3. Elige número de componentes o % varianza
4. Visualiza Scree Plot
5. Aplica transformación
```

**Selección de Características:**
```
1. Elige método:
   - Variance Threshold
   - Correlation-based
   - Feature Importance
   - RFE
2. Define parámetros
3. Revisa características seleccionadas
```

## Quizzes

### Tomar un Quiz

1. Dashboard → "Quizzes"
2. Selecciona módulo:
   - Limpieza de Datos
   - Transformación de Datos
   - Integración de Datos
   - Reducción de Dimensionalidad
3. Lee instrucciones
4. Tienes **15 minutos** para completar
5. 12 preguntas de opción múltiple

### Durante el Quiz

- **Temporizador**: Visible en la esquina superior derecha
- **Progreso**: Barra muestra preguntas respondidas
- **Navegación**: Puedes ir hacia atrás y adelante
- **Guardar**: Respuestas se guardan automáticamente

### Resultados

Después de enviar:
- **Puntuación**: Porcentaje de respuestas correctas
- **Revisión detallada**: 
  - Tu respuesta
  - Respuesta correcta
  - Explicación de cada pregunta
- **Recomendaciones**: Temas a repasar

**Criterios de Evaluación:**
- 90-100%: Excelente ✅
- 70-89%: Buen trabajo 👍
- <70%: Necesitas repasar 📚

## Exportación de Datos

### Exportar Dataset Procesado

1. Después de aplicar transformaciones
2. Haz clic en "Exportar"
3. Selecciona formato:
   - **CSV**: Compatible con Excel, Python, R
   - **Excel**: Formato .xlsx con formato
   - **JSON**: Para APIs y aplicaciones web

### Exportar Reporte de Análisis

1. Haz clic en "Exportar Reporte"
2. Descarga archivo JSON con:
   - Información del dataset
   - Estadísticas descriptivas
   - Calidad de datos
   - Valores faltantes
   - Duplicados

## Consejos y Mejores Prácticas

### Para Aprender Efectivamente

1. **Sigue el orden**: Teoría → Práctica → Quiz
2. **Toma notas**: Anota conceptos clave
3. **Experimenta**: Prueba diferentes técnicas
4. **Compara resultados**: Antes y después de cada operación
5. **Repite quizzes**: Hasta dominar el tema

### Para el Laboratorio

1. **Explora primero**: Usa visualizaciones antes de transformar
2. **Documenta cambios**: Anota qué hiciste y por qué
3. **Valida resultados**: Verifica que las transformaciones sean correctas
4. **Guarda pipelines**: Para reutilizar en otros datasets
5. **Exporta frecuentemente**: No pierdas tu trabajo

### Errores Comunes a Evitar

❌ **NO hacer:**
- Eliminar outliers sin investigar
- Aplicar PCA sin estandarizar
- Usar One-Hot con muchas categorías
- Hacer joins sin validar claves
- Imputar sin entender el patrón de nulos

✅ **SÍ hacer:**
- Explorar datos antes de limpiar
- Entender el contexto del dominio
- Validar cada transformación
- Documentar decisiones
- Comparar múltiples enfoques

### Atajos de Teclado

- `Ctrl + S`: Guardar pipeline
- `Ctrl + E`: Exportar datos
- `Ctrl + Z`: Deshacer última operación
- `Ctrl + R`: Recargar dataset original

## Recursos Adicionales

### Dentro de la Plataforma

- **Teoría**: Explicaciones detalladas con ejemplos
- **Ejemplos interactivos**: En cada módulo de teoría
- **Tooltips**: Pasa el mouse sobre íconos ℹ️
- **Mensajes de error**: Incluyen sugerencias de solución

### Datasets Recomendados para Practicar

1. **Principiantes**: Iris, Wine
2. **Intermedio**: Titanic, Customer Data
3. **Avanzado**: California Housing, Sales Transactions

### Progresión Sugerida

**Semana 1**: Limpieza de Datos
- Leer teoría
- Practicar con Titanic dataset
- Completar quiz

**Semana 2**: Transformación de Datos
- Leer teoría
- Practicar con Wine dataset
- Completar quiz

**Semana 3**: Integración de Datos
- Leer teoría
- Practicar con Sales Transactions
- Completar quiz

**Semana 4**: Reducción de Dimensionalidad
- Leer teoría
- Practicar con California Housing
- Completar quiz

## Soporte

Si encuentras problemas:
1. Revisa esta guía
2. Consulta la teoría del módulo relevante
3. Verifica mensajes de error
4. Contacta al instructor

## Actualizaciones

Esta plataforma se actualiza regularmente con:
- Nuevos datasets
- Más técnicas de preprocesamiento
- Quizzes adicionales
- Mejoras en visualizaciones

---

=======
# Guía de Usuario - Plataforma de Preprocesamiento de Datos

## 📚 Tabla de Contenidos
1. [Introducción](#introducción)
2. [Primeros Pasos](#primeros-pasos)
3. [Módulos de Teoría](#módulos-de-teoría)
4. [Laboratorio Práctico](#laboratorio-práctico)
5. [Quizzes](#quizzes)
6. [Exportación de Datos](#exportación-de-datos)
7. [Consejos y Mejores Prácticas](#consejos-y-mejores-prácticas)

## Introducción

Esta plataforma está diseñada para ayudarte a aprender y practicar técnicas de preprocesamiento de datos en minería de datos. Incluye:

- **Teoría completa** sobre 4 temas principales
- **Laboratorio interactivo** para practicar con datos reales
- **Quizzes** para evaluar tu conocimiento
- **Datasets precargados** para experimentar
- **Visualizaciones** para análisis exploratorio

## Primeros Pasos

### 1. Registro e Inicio de Sesión

1. Accede a la página principal
2. Haz clic en "Registrarse"
3. Completa el formulario con:
   - Nombre de usuario
   - Email
   - Contraseña
4. Inicia sesión con tus credenciales

### 2. Dashboard

Después de iniciar sesión, verás tu dashboard con:
- **Progreso general**: Porcentaje de módulos completados
- **Módulos disponibles**: Teoría y práctica de cada tema
- **Estadísticas**: Tiempo dedicado y quizzes completados

## Módulos de Teoría

### Limpieza de Datos

Aprende sobre:
- **Valores nulos**: Detección y métodos de imputación
- **Duplicados**: Identificación y eliminación
- **Outliers**: Detección con IQR, Z-score e Isolation Forest
- **Mejores prácticas**: Cuándo y cómo aplicar cada técnica

**Navegación:**
1. Dashboard → "Teoría" → "Limpieza de Datos"
2. Lee el contenido completo
3. Toma notas de los conceptos clave
4. Practica con los ejemplos

### Transformación de Datos

Cubre:
- **Normalización**: Min-Max, Standard, Robust, Max Abs
- **Encoding**: One-Hot, Label, Ordinal, Target
- **Cuándo usar cada método**
- **Ventajas y desventajas**

### Integración de Datos

Incluye:
- **Tipos de Joins**: Inner, Left, Right, Outer
- **Merge vs Concat**: Diferencias y casos de uso
- **Validación**: Cómo verificar resultados
- **Problemas comunes**: Duplicados, pérdida de datos

### Reducción de Dimensionalidad

Explica:
- **PCA**: Análisis de Componentes Principales
- **Selección de características**: Filter, Wrapper, Embedded
- **Comparación**: PCA vs Selección
- **Aplicaciones prácticas**

## Laboratorio Práctico

### Cargar Datos

**Opción 1: Datasets Precargados**
1. Ve a "Práctica" → "Laboratorio"
2. Selecciona un dataset del menú desplegable:
   - Iris (clasificación)
   - Titanic (limpieza de datos)
   - Wine (transformación)
   - California Housing (regresión)
   - Customer Data (calidad de datos)
   - Sales Transactions (integración)

**Opción 2: Subir tu Propio Dataset**
1. Haz clic en "Subir Dataset"
2. Selecciona archivo CSV o Excel
3. Espera la confirmación de carga

### Análisis Exploratorio

**Visualizaciones Disponibles:**

1. **Boxplot**: Detectar outliers
   - Selecciona columna numérica
   - Observa valores atípicos

2. **Histogram**: Distribución de datos
   - Elige columna
   - Ajusta número de bins

3. **Scatter Plot**: Relaciones entre variables
   - Selecciona X e Y
   - Opcional: color por categoría

4. **Heatmap**: Correlaciones
   - Muestra relaciones entre todas las variables numéricas
   - Identifica multicolinealidad

5. **Pairplot**: Múltiples relaciones
   - Visualiza todas las combinaciones
   - Útil para exploración inicial

### Operaciones de Limpieza

**Imputación de Valores Nulos:**
```
1. Selecciona columna con valores nulos
2. Elige método:
   - Media (datos numéricos simétricos)
   - Mediana (datos con outliers)
   - Moda (datos categóricos)
   - KNN (considera relaciones)
   - Forward/Backward Fill (series temporales)
3. Aplica y verifica resultados
```

**Eliminación de Duplicados:**
```
1. Haz clic en "Detectar Duplicados"
2. Revisa filas duplicadas
3. Decide: eliminar o mantener
4. Confirma operación
```

**Tratamiento de Outliers:**
```
1. Selecciona método de detección:
   - IQR (robusto, no asume normalidad)
   - Z-score (asume normalidad)
   - Isolation Forest (alta dimensionalidad)
2. Visualiza outliers detectados
3. Decide: eliminar, transformar o mantener
```

### Operaciones de Transformación

**Normalización:**
```
1. Selecciona columnas numéricas
2. Elige método:
   - Min-Max: rango [0,1]
   - Standard: media=0, std=1
   - Robust: usa mediana e IQR
   - Max Abs: rango [-1,1]
3. Aplica y compara distribuciones
```

**Encoding:**
```
1. Selecciona columnas categóricas
2. Elige método:
   - One-Hot: variables nominales
   - Label: variables ordinales
   - Ordinal: con orden específico
   - Target: basado en variable objetivo
3. Verifica nuevas columnas creadas
```

### Integración de Datos

**Joins:**
```
1. Carga dos datasets
2. Selecciona columnas clave
3. Elige tipo de join:
   - Inner: solo coincidencias
   - Left: todas de izquierda
   - Right: todas de derecha
   - Outer: todas de ambas
4. Valida resultado
```

### Reducción de Dimensionalidad

**PCA:**
```
1. Selecciona características numéricas
2. Estandariza datos (importante!)
3. Elige número de componentes o % varianza
4. Visualiza Scree Plot
5. Aplica transformación
```

**Selección de Características:**
```
1. Elige método:
   - Variance Threshold
   - Correlation-based
   - Feature Importance
   - RFE
2. Define parámetros
3. Revisa características seleccionadas
```

## Quizzes

### Tomar un Quiz

1. Dashboard → "Quizzes"
2. Selecciona módulo:
   - Limpieza de Datos
   - Transformación de Datos
   - Integración de Datos
   - Reducción de Dimensionalidad
3. Lee instrucciones
4. Tienes **15 minutos** para completar
5. 12 preguntas de opción múltiple

### Durante el Quiz

- **Temporizador**: Visible en la esquina superior derecha
- **Progreso**: Barra muestra preguntas respondidas
- **Navegación**: Puedes ir hacia atrás y adelante
- **Guardar**: Respuestas se guardan automáticamente

### Resultados

Después de enviar:
- **Puntuación**: Porcentaje de respuestas correctas
- **Revisión detallada**: 
  - Tu respuesta
  - Respuesta correcta
  - Explicación de cada pregunta
- **Recomendaciones**: Temas a repasar

**Criterios de Evaluación:**
- 90-100%: Excelente ✅
- 70-89%: Buen trabajo 👍
- <70%: Necesitas repasar 📚

## Exportación de Datos

### Exportar Dataset Procesado

1. Después de aplicar transformaciones
2. Haz clic en "Exportar"
3. Selecciona formato:
   - **CSV**: Compatible con Excel, Python, R
   - **Excel**: Formato .xlsx con formato
   - **JSON**: Para APIs y aplicaciones web

### Exportar Reporte de Análisis

1. Haz clic en "Exportar Reporte"
2. Descarga archivo JSON con:
   - Información del dataset
   - Estadísticas descriptivas
   - Calidad de datos
   - Valores faltantes
   - Duplicados

## Consejos y Mejores Prácticas

### Para Aprender Efectivamente

1. **Sigue el orden**: Teoría → Práctica → Quiz
2. **Toma notas**: Anota conceptos clave
3. **Experimenta**: Prueba diferentes técnicas
4. **Compara resultados**: Antes y después de cada operación
5. **Repite quizzes**: Hasta dominar el tema

### Para el Laboratorio

1. **Explora primero**: Usa visualizaciones antes de transformar
2. **Documenta cambios**: Anota qué hiciste y por qué
3. **Valida resultados**: Verifica que las transformaciones sean correctas
4. **Guarda pipelines**: Para reutilizar en otros datasets
5. **Exporta frecuentemente**: No pierdas tu trabajo

### Errores Comunes a Evitar

❌ **NO hacer:**
- Eliminar outliers sin investigar
- Aplicar PCA sin estandarizar
- Usar One-Hot con muchas categorías
- Hacer joins sin validar claves
- Imputar sin entender el patrón de nulos

✅ **SÍ hacer:**
- Explorar datos antes de limpiar
- Entender el contexto del dominio
- Validar cada transformación
- Documentar decisiones
- Comparar múltiples enfoques

### Atajos de Teclado

- `Ctrl + S`: Guardar pipeline
- `Ctrl + E`: Exportar datos
- `Ctrl + Z`: Deshacer última operación
- `Ctrl + R`: Recargar dataset original

## Recursos Adicionales

### Dentro de la Plataforma

- **Teoría**: Explicaciones detalladas con ejemplos
- **Ejemplos interactivos**: En cada módulo de teoría
- **Tooltips**: Pasa el mouse sobre íconos ℹ️
- **Mensajes de error**: Incluyen sugerencias de solución

### Datasets Recomendados para Practicar

1. **Principiantes**: Iris, Wine
2. **Intermedio**: Titanic, Customer Data
3. **Avanzado**: California Housing, Sales Transactions

### Progresión Sugerida

**Semana 1**: Limpieza de Datos
- Leer teoría
- Practicar con Titanic dataset
- Completar quiz

**Semana 2**: Transformación de Datos
- Leer teoría
- Practicar con Wine dataset
- Completar quiz

**Semana 3**: Integración de Datos
- Leer teoría
- Practicar con Sales Transactions
- Completar quiz

**Semana 4**: Reducción de Dimensionalidad
- Leer teoría
- Practicar con California Housing
- Completar quiz

## Soporte

Si encuentras problemas:
1. Revisa esta guía
2. Consulta la teoría del módulo relevante
3. Verifica mensajes de error
4. Contacta al instructor

## Actualizaciones

Esta plataforma se actualiza regularmente con:
- Nuevos datasets
- Más técnicas de preprocesamiento
- Quizzes adicionales
- Mejoras en visualizaciones

---

>>>>>>> 5cacc14741e04989bfeb01a4c6f9a705353a88f4
**¡Buena suerte en tu aprendizaje! 🚀**