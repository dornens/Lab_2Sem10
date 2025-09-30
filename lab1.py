# ==============================
# Laboratorio 2 – Segundo Cómputo
# Semana 10 – Pandas (Top 500 Songs)
# ==============================

import pandas as pd
import numpy as np

# Cargamos la dataset con la codificación correcta que es latin1 ya que da error sin ella
df = pd.read_csv("Top_500_Songs.csv", encoding="latin1")

#Resumen estadístico (solo aplica a columnas numéricas, aquí pocas son numéricas)
print("=== Resumen estadístico con describe() ===")
print(df.describe(include="all"))

#Identificacion tipos de datos
print("\n=== Tipos de datos (dtypes) ===")
print(df.dtypes)

#Mostrar primeros y últimos registros
print("\n=== Primeros registros (head) ===")
print(df.head())
print("\n=== Últimos registros (tail) ===")
print(df.tail())

#Ordenar resultados por semanas en lista (columna 'streak')
# Nota: hay que limpiar la columna porque es texto como "12 weeks"
df["weeks_on_chart"] = df["streak"].str.extract(r"(\d+)").astype(float)

print("\n=== Canciones con mayor tiempo en lista ===")
print(df.sort_values(by="weeks_on_chart", ascending=False)[["title","artist","weeks_on_chart"]].head(10))

#Medidas estadísticas sobre semanas en lista
media = np.mean(df["weeks_on_chart"])
mediana = np.median(df["weeks_on_chart"])
desviacion = np.std(df["weeks_on_chart"])

print("\n=== Medidas estadísticas de la columna 'weeks_on_chart' ===")
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Desviación estándar: {desviacion}")
