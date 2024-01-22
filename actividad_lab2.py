# -*- coding: utf-8 -*-
import cargador_animales as c
def promedio_patas(animales:list)->float:
    suma = 0
    i = 0
    
    while i<len(animales):
        suma += animales[i]['legs']
        i += 1
    

    return suma/len(animales)

lista = c.cargar_animales("zoo.csv")
prom = promedio_patas(lista)
print("El promedio de patas es: " + str(prom))