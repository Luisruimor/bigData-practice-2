import pandas as pd

#Leo el archivo 'data.csv' y lo guardo en una variable
initialCSV = pd.read_csv('data.csv')

#Imprimo los 5 primeros registros, el método .head() por defecto (si no le pasas ningun argumento) imprime 5 registros
print("-------Primeros 5 registros------- ")
print(initialCSV.head())

#Imprime informacion general de las columnas y el numero de filas
print("-------Descripcion de las filas y columnas------- ")
initialCSV.info()

#Imprimimos un subconjunto de las 4 primeras columnas
print("-------Subconjunto de las 4 primeras columnas------- ")
print(initialCSV.iloc[:,0:4])

#Creo una variable que es el dataset ordenado por Vaccine
vaccineCSV = initialCSV.sort_values('Vaccine')

#Exporto el dataset ordenado como un archivo .csv
vaccineCSV.to_csv('dataVaccineOrder.csv')