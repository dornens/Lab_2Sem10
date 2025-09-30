# ==============================
# Laboratorio 2 – Segundo Cómputo
# Semana 10 – Pandas
# ==============================

# Importar librerías necesarias
import pandas as pd
import numpy as np

# 1. Cargar dataset descargado de Kaggle (ejemplo: dataset de ventas)
# Cambiar "dataset.csv" por el archivo que elegiste
df = pd.read_csv("Top_500_Songs.csv", encoding="latin-1")

# 2. Resumen estadístico del dataset
print("=== Resumen estadístico con describe() ===")
print(df.describe())

# 3. Identificar tipos de datos
print("\n=== Tipos de datos (dtypes) ===")
print(df.dtypes)

# 4. Mostrar primeros y últimos registros
print("\n=== Primeros registros (head) ===")
print(df.head())
print("\n=== Últimos registros (tail) ===")
print(df.tail())

# 5. Ordenar resultados por una columna (ejemplo: ventas)
print("\n=== Datos ordenados por columna 'ventas' de forma descendente ===")
print(df.sort_values(by="ventas", ascending=False).head(10))

# 6. Medidas estadísticas sobre una columna (ejemplo: 'ventas')
columna = "ventas"

media = np.mean(df[columna])
mediana = np.median(df[columna])
desviacion = np.std(df[columna])

print(f"\n=== Medidas estadísticas de la columna '{columna}' ===")
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Desviación estándar: {desviacion}")
