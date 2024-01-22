# -*- coding: utf-8 -*-
import cargador_animales as c
def animales_con_doble_w_no_ini_fin(animales:list)->int:
    
    cant = 0
    i = 0
    while i<len(animales):
        if 'w' in animales[i]['animal_name'][1:-1]:
            cant=+1
        i+=1
    return cant



lista = c.cargar_animales("zoo.csv")
cuantos = animales_con_doble_w_no_ini_fin(lista)
print("Hay  " + str(cuantos) + " animales que contienen w en el nombre (no al inicio ni al final)")