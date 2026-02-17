import pandas as pd
import matplotlib.pyplot as plt

#Cargar el csv
df = pd.read_csv("restaurantes_la_dorada_caldas.csv")

#Mostrar las primeras filas del dataframe
print(df.head()), 
print("\n"),
print(df.info()),
print("\n"),
print(df.describe()),
print("\n"),
print(df.isnull().sum())

#Convertir nombres de columnas a minúsculas y reemplazar espacios por guiones bajos
df.columns = df.columns.str.lower().str.replace(' ', '_')

#Identificar las columnas que tengan valores nulos
nulos = df.isnull().sum()

#Porcentaje de nulos
porcentaje_nulos = (df.isnull().mean() * 100).round(2)

#Resumen de las columnas con nulos
resumen_nulos = pd.DataFrame({
    "nulos": nulos,
    "porcentaje_nulos": porcentaje_nulos
}).sort_values(by = "porcentaje_nulos", ascending=False)
print(resumen_nulos)