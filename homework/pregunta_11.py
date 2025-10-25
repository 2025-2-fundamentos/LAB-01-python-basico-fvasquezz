"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv
ruta=r'C:\Users\Arquitecto\Documents\GitHub\LAB-01-python-basico-fvasquezz\files\input\data.csv'


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    datos=cargar_datos(ruta)
    lista=crear_lista(datos)
    dic={}
    for i in lista:
        for elemento in i:
            if elemento not in dic and elemento!=i[-1]:
                dic[elemento]=int(i[-1])
            elif elemento in dic and elemento!=i[-1]:
                dic[elemento]+=int(i[-1])
    dic=list(dic.items())
    dic.sort()
    dic=dict(dic)

    return dic

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

def crear_lista(x):
    lista=[]
    for i in x:
        elemento=i[3] +","+ i[1]
        elemento=elemento.split(",")
        lista.append(elemento)
    return lista
