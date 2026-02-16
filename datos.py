import pandas as pd
import matplotlib.pyplot as plt

#Cargar el csv
df = pd.read_csv("restaurantes_la_dorada_caldas.csv")

#Mostrar las primeras filas del dataframe
print(df.head())