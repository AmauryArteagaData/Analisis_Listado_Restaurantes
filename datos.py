import pandas as pd
import matplotlib.pyplot as plt

import re
from phonenumbers import PhoneNumberFormat



#FASE 1: CARGA Y EXPLORACIÓN DE LOS DATOS
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

#FASE 2: LIMPIEZA DE LOS DATOS
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

print("\n")

#Tipos de datos
#mostrar la columna de teléfono
print(df["teléfono"].head(5))
print("\n")

print(df["teléfono"].dropna().sample(10))

print("\n")
#Eliminar caracteres no numéricos de la columna teléfono
def limpiar_telefono(numero):
    if pd.isnull(numero):
        return None
    
#Convertir a string y eliminar caracteres no numéricos
    numero = str(numero)
    numero = re.sub(r'\D', '', numero)
    return numero

df["teléfono_limpio"] = df["teléfono"].apply(limpiar_telefono)
print(df["teléfono_limpio"].head(5))

#Quitar la columna original de teléfono
df = df.drop(columns=["teléfono"], axis=1)

print("\n")
#Eliminar duplicados
df = df.drop_duplicates()

#Exportar el dataframe limpio a un nuevo archivo CSV
df.to_csv("restaurantes_la_dorada_caldas_limpio.csv", index=False)

