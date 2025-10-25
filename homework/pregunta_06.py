"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv
ruta=r'C:\Users\Arquitecto\Documents\GitHub\LAB-01-python-basico-fvasquezz\files\input\data.csv'

def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    datos=cargar_datos(ruta)
    lista_final=limpieza_5columna(datos)

    A={}
    for i in lista_final:
        key=i[0]
        valor=int(i[1])
        if i[0] not in A:
            A[key]=[valor,valor]
        elif valor>A[key][1]:
            A[key][1]=valor
        elif valor<A[key][0]:
            A[key][0]=valor 
    A=list(A.items())

    B=[]
    for i in A:
        B.append((i[0],i[1][0],i[1][1]))
    return B

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