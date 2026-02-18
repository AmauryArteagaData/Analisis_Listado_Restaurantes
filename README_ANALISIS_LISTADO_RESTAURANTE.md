Este README.md fue creado con ChatGPT con motivos estrictamente educativos.

# 📊 Proyecto de Análisis de Datos  
## Dataset: LISTADO_DE_RESTAURANTES_EN_LA_DORADA_CALDAS
---
# 🎯 Objetivo del Proyecto

Realizar un análisis completo del dataset de restaurantes con enfoque profesional, aplicando:

- Exploración y limpieza con Python
- Consultas avanzadas en SQL
- Construcción de dashboard en Looker Studio
- Análisis crítico empresarial
---
# 🧩 FASE 1 — Exploración Inicial (Python)
## 1. Carga y análisis preliminar

Tareas:
- Cargar el CSV usando pandas
- Ejecutar:
  - `df.head()`
  - `df.info()`
  - `df.describe()`
  - `df.isnull().sum()`
- Identificar:
  - Tipos de datos incorrectos
  - Columnas irrelevantes
  - Registros duplicados
  - Inconsistencias en texto

### Entregable
Documento breve explicando:

- Número total de registros
- Número total de columnas
- Columnas con mayor porcentaje de valores nulos
- Primeras observaciones técnicas
---
# 🧹 FASE 2 — Limpieza de Datos
## 1. Normalización

- Convertir nombres de columnas a minúsculas
- Reemplazar espacios por "_"
- Estandarizar textos (strip, lower o upper según convenga)

## 2. Manejo de datos faltantes
- Identificar columnas con más del 20% de nulos
- Decidir:
  - Eliminar registros
  - Imputar
  - Mantener y justificar

## 3. Tipos de datos
- Convertir columnas numéricas mal tipadas
- Validar latitud/longitud si existen
- Revisar formato de teléfonos

## 4. Eliminación de duplicados
- Identificar duplicados completos
- Identificar duplicados por nombre + dirección

### Entregable
Exportar dataset limpio como: restaurantes_clean.csv
---
# 📈 FASE 3 — Análisis en Python
## 1. Análisis descriptivo
- Conteo total de restaurantes

## 2. Detección de patrones

- Nombres repetidos
- Posibles inconsistencias
- Outliers en variables numéricas

## 3. Visualizaciones obligatorias

Crear:

- Gráfico de barras
- Gráfico de pastel
- Histograma
- Gráfico de dispersión

Reglas:
- No usar colores personalizados
- Cada gráfico debe tener título y etiquetas claras
---
# 🗄️ FASE 4 — SQL
Importar el dataset limpio y crear la tabla:

```sql
CREATE TABLE restaurantes (
    id INT PRIMARY KEY,
    nombre VARCHAR(150),
    categoria VARCHAR(100),
    direccion VARCHAR(200),
    telefono VARCHAR(50),
    latitud FLOAT,
    longitud FLOAT
);
