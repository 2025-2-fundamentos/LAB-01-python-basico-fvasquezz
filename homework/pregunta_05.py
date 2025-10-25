"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv
ruta=r'C:\Users\Arquitecto\Documents\GitHub\LAB-01-python-basico-fvasquezz\files\input\data.csv'

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """

    datos=cargar_datos(ruta)
    datos.sort()
    lista={}

    for i in datos:
        letra=i[0]
        valor=int(i[1])
        if letra not in lista:
            lista[letra]=[valor,valor]
        if letra in lista:
            if valor>lista[letra][0]:
                lista[letra][0]=valor
            elif valor<lista[letra][1]:
                lista[letra][0]=valor
    lista=list(lista.items())

    lista_nueva=[]
    for i in lista:
        tupla=(i[0],i[1][0],i[1][1])
        lista_nueva.append(tupla)
    return lista_nueva


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