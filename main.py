from lectura import *

lector = CSVReader('datos.csv')

columna = lector.leer_columna(1)

for fila in lector.recorrer():
    print(fila)
