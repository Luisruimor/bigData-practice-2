# Caso Práctico 2
Caso práctico de la asignatura de BigData para la transformacion de la empresa de la Universidad Nebrija,
Es un caso muy sencillo de manipulacion de un dataset, utilizando la libreria pandas.
El dataset que utilizaremos será [este](data.csv) , descargado de la web: https://www.ecdc.europa.eu/en/publications-data/data-covid-19-vaccination-eu-eea

## ROADMAP

- [x] Lea la información contenida en el archivo .csv (función: .read_csv) y guárdelo
en una variable.
- [x] Muestra la información de los primeros 5 registros (función: head).
- [x] Obtenga una descripción de las filas y columnas del conjunto de
datos.
- [x] Seleccione y muestre las 4 primeras columnas (manipulación de
datos).
- [x] Ordene los registros por Vaccine (función: .sort_values())
- [x] Exporte el CSV resultado después de ser ordenado por Vaccine. [**El dataset exportado**](dataVaccineOrder.csv)