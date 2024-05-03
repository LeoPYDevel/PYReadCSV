import csv

class CSVReader:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo

    def leer_fila(self, numero_fila):
        with open(self.nombre_archivo, 'r') as archivo:
            lector_csv = csv.reader(archivo)
            for i, fila in enumerate(lector_csv, start=1):
                if i == numero_fila:
                    return fila

    def leer_columna(self, numero_columna):
        with open(self.nombre_archivo, 'r') as archivo:
            lector_csv = csv.reader(archivo)
            columnas = zip(*lector_csv)
            for i, columna in enumerate(columnas, start=1):
                if i == numero_columna:
                    return list(columna)

    def recorrer(self):
        with open(self.nombre_archivo, 'r') as archivo:
            lector_csv = csv.reader(archivo)
            for fila in lector_csv:
                yield fila

# Ejemplo de uso
def main():
    nombre_archivo = 'datos.csv'
    lector = CSVReader(nombre_archivo)

    columna = lector.leer_columna(2)
    
    print(f"\nColumna:", columna)

if __name__ == "__main__":
    main()
