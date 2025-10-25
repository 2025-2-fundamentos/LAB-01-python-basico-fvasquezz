"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv
ruta=r'C:\Users\Arquitecto\Documents\GitHub\LAB-01-python-basico-fvasquezz\files\input\data.csv'


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
    datos=cargar_datos(ruta)

    datos.sort()
    lista={}

    for i in datos:
        letra=i[0]
        if letra not in lista:
            lista[letra]=int(i[1])
        elif letra in lista:
            lista[letra]+=int(i[1])
    lista=list(lista.items())
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

