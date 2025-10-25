"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv
ruta = "files/input/data.csv"

def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    datos=cargar_datos(ruta)
    lista_final=limpieza_5columna(datos)
    dic={}
    for i in lista_final:
        key=i[0]
        if key not in dic:
            dic[key]=1
        else:
            dic[key]+=1
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

def limpieza_5columna(x):
    nueva_lista=[]
    lista_final=[]
    #Separación de los elementos de la quinta fila por comas 
    for i in x:
        elemento=i[4]
        elemento=elemento.split(",")
    #Pegarlos en la nueva lista cada uno como un nuevo elemento de la lista
        nueva_lista.extend(elemento)

    for i in nueva_lista:
    #Separar cada "llave" de su valor y pegarlo a una nueva lista
        elemento=i
        elemento=elemento.split(":")
        lista_final.append(elemento)
    lista_final.sort()
    
    return lista_final