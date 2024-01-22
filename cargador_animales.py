# -*- coding: utf-8 -*-
def cargar_animales(archivo:str)->list:
    """
    Carga el archivo excel de animales.

    Parameters
    ----------
    archivo : str
        Ruta del archivo que se desea cargar.

    Returns
    -------
    list
        lista con los diccionarios de los animales cargados.

    """
    animales = []
    
    archivo = open(archivo, "r")
    
    encabezados = archivo.readline()
    linea = archivo.readline()
    
    while len(linea) > 0:
        animales.append(crear_animal(encabezados, linea))
        linea = archivo.readline();
        
    return animales

def crear_animal(encabezados: str, linea:str)->dict:
    """
    Crea un diccionario con la información de 
    un animal a partir de los parámetros recibidos

    Parameters
    ----------
    encabezados : str
        Llaves del diccionario
    linea : str
        datos del diccionario

    Returns
    -------
    dict
        diccionario con la información del animal

    """
    animal = {}
    
    encs = encabezados.split(";")
    dat = linea.split(";")
    
    i = 0
    
    while i < len(encs):
        dato = dat[i].replace("\n", "")
        
        try:
            dato = int(dat[i])
            if dato <= 1 and encs[i] != 'legs':
                dato = bool(dato)
        except:
            dato = dat[i].replace("\n", "")

        animal[encs[i].replace("\n","")] = dato
        i+=1
    
    return animal
    
l = cargar_animales("zoo.csv")