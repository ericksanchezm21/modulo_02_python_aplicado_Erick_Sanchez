# Proyecto Final: Pipeline Básico de Procesamiento de Datos

"""
Antes de proceder con el codigo en python, se debe de correr este comando en la terminal 
(aplicable para powershell):

Invoke-WebRequest -Uri "https://raw.githubusercontent.com/reisanar/datasets/master/HollywoodMovies.csv" -OutFile hollywood.csv
"""

# ----- Etapa 0: Importar librerias necesarias para trabajar -----

import pandas as pd

# ----- Etapa 1: Cargar y diagnosticar -----

print("Ejecucion de la etapa 1")
print("")

# Leer archivo "hollywood.csv" por medio de pandas y almacenar datos en una variable llamada "df"
df = pd.read_csv("hollywood.csv")
print("-DataFrame cargado-")
print("")

# Modificar el dataframe cargado para que este conserve las columnas de interes
df = df[["Movie", "LeadStudio", "Genre", "RottenTomatoes", "AudienceScore", "WorldGross", "Budget", "Year"]]
print("-DataFrame modificado con las columnas que se van a trabajar-")
print("")

# Hacer diagnostico inicial (cantidad de filas y columnas, y valores null por columna)
print("Diagnostico inicial del dataframe:")
print("")
print("Estas son las dimensiones del dataframe en su estado actual:", df.shape)
print("")
print("-----Cantidad de nulls presentes en el dataframe por columna-----")
print(df.isnull().sum())
print("")
print("Total de valores nulls presentes:", df.isnull().sum().sum())
print("")
print("Etapa 1 terminada.")
print("")
print("------------------------------------------------------------------------")

# ----- Etapa 2: Limpiar -----

print("Ejecucion de la etapa 2")
print("")

# Rellenar los valores null de las columnas "Genre" y "LeadStudio"
df["Genre"] = df["Genre"].fillna(value = "Other Genres")
df["LeadStudio"] = df["LeadStudio"].fillna(value = "Other Lead Studios")
print("-Rellenado de valores null en las columnas Genre y LeadStudio completado.-")
print("")

# Rellenar los valores null de las columnas "RottenTomatoes" y "AudienceScore"
mediana_rotten_tomatoes = df["RottenTomatoes"].median()
mediana_audience_score = df["AudienceScore"].median()
df["RottenTomatoes"] = df["RottenTomatoes"].fillna(value = mediana_rotten_tomatoes)
df["AudienceScore"] = df["AudienceScore"].fillna(value = mediana_audience_score)
print("-Rellenado de valores null en las columnas RottenTomatoes y AudienceScore completado.-")
print("")

# Eliminar registros que contengan valores null tanto en la columna "WorldGross" como en la columna "Budget"
df = df.dropna(subset = ["WorldGross", "Budget"])
print("-Eliminacion de registros con valores null tanto en las columnas WorldGross como Budget terminado.-")
print("")

print("Diagnostico del dataframe luego de la limpieza:")
print("")
print("Estas son las dimensiones del dataframe luego de la limpieza:", df.shape)
print("")
print("-----Cantidad de nulls presentes en el dataframe por columna luego de la limpieza-----")
print(df.isnull().sum())
print("")
print("Total de valores nulls presentes:", df.isnull().sum().sum())
print("")
print("Etapa 2 terminada.")
print("")
print("------------------------------------------------------------------------")

# ----- Etapa 3: Crear columnas nuevas -----

print("Ejecucion de la etapa 3")
print("")

# Crear la columna Ganancia (WorldGross - Budget)
df["Ganancia"] = df["WorldGross"] - df["Budget"]
print("-Creacion de columna Ganancia completada.-")
print("")

# Crear la columna Exitosa (una pelicula se considera exitosa si tiene en Rotten Tomatoes una calificacion de 60 en adelante)
df["Exitosa"] = df["RottenTomatoes"] >= 60
print("-Creacion de columna Exitosa completada.-")
print("")

# Hacer conteo de peliculas exitosas y no exitosas (Los valores True son peliculas exitosas y los valores False son las no exitosas)
print("-Conteo de peliculas exitosas y no exitosas.-")
print(df["Exitosa"].value_counts())
print("")
print("Etapa 3 terminada.")
print("")
print("------------------------------------------------------------------------")

# ----- Etapa 4: Tipos de datos y ordenar -----

print("Ejecucion de la etapa 4")
print("")

# Confirmar el tipo de dato de los valores de la columna Exitosa
print("El tipo de dato de los valores de la columna Exitosa es:", df["Exitosa"].dtype)
print("")

# Ordenar los registros del dataset por la ganancia de la pelicula (de mayor a menor)
df = df.sort_values(by = "Ganancia", ascending= False)
print("-Ordenacion del dataframe por la columna Ganancia de forma descendente realizado.-")
print("")

# Obtener el top 3 de peliculas con mayores ganancias (reflejar nombre de la pelicula y ganancia)
print("-----Este es el top 3 de peliculas con mayores ganancias-----")
print(df[["Movie", "Ganancia"]].head(3))
print("")
print("Etapa 4 terminada.")
print("")
print("------------------------------------------------------------------------")

# ----- Etapa 5: Agrupar y analizar -----

print("Ejecucion de la etapa 5")
print("")

# Calculo de la calificacion promedio de Rotten Tomatoes por cada genero de pelicula (los valores deben de estar redondeados a 1 decimal)
print("-----Calificacion promedio de Rotten Tomatoes por genero de pelicula-----")
print("")
df_agrupado_genero = round(df.groupby(by = "Genre")["RottenTomatoes"].mean(),1)
print(df_agrupado_genero)
print("")

# Calculo de la ganancia promedio por estudio (los valores deben de estar redondeados a 1 decimal)
print("-----Ganancia promedio por estudio-----")
print("")
df_agrupado_estudio = round(df.groupby(by = "LeadStudio")["Ganancia"].mean(),1)
print(df_agrupado_estudio)
print("")

# Imprimir genero con mayor calificacion
print("-Este es el genero con mayor calificacion.-")
print(df_agrupado_genero.sort_values(ascending = False).head(1))
print("")
genero_mayor_calificacion = df_agrupado_genero.sort_values(ascending = False).head(1).index[0]
print("Total de peliculas de ese genero:", len(df[df["Genre"] == genero_mayor_calificacion]))
print("")
print("Etapa 5 terminada.")
print("")
print("------------------------------------------------------------------------")

# ----- Etapa 6: Guardar el resultado -----

print("Ejecucion de la etapa 6")
print("")

# Guardar el dataframe limpio en un archivo .csv con el nombre hollywood_limpio.csv sin la columna extra de indice
df.to_csv("hollywood_limpio.csv", index = False)
print("-DataFrame limpio guardado en un nuevo archivo csv-")
print("")
df_limpio = pd.read_csv("hollywood_limpio.csv")
print("Estas son las dimensiones del nuevo dataframe:", df_limpio.shape)
print("")
print("-Aqui esta el dianostico de nulls del nuevo dataframe.-")
print(df_limpio.isnull().sum())
print("")
print("Total de valores nulls presentes:", df_limpio.isnull().sum().sum())
print("")
print("Etapa 6 terminada.")
print("")
print("------------------------------------------------------------------------")

