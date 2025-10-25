"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv
ruta=r'C:\Users\Arquitecto\Documents\GitHub\LAB-01-python-basico-fvasquezz\files\input\data.csv'

def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
    datos=cargar_datos(ruta)
    lista=[]
    for i in datos:
        clave=i
        valor1=len(clave[3].split(","))
        valor2=len(clave[4].split(","))
        fila=(i[0],valor1,valor2)
        lista.append(fila)
    return lista
    



def cargar_datos(ruta_del_archivo):
    datos = []
    #El CSV estaba separado por tabulaciones no por comas, por eso se hace delimiter='\t'
    try:
        with open(ruta_del_archivo, mode='r', encoding='utf-8', newline='') as archivo:
            lector = csv.reader(archivo,delimiter='\t')

            for fila in lector:
                datos.append(fila)
                
    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el archivo en la ruta:\n{ruta_del_archivo}")
        return None
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return None
    
        
    return datos
