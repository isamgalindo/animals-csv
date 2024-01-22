# -*- coding: utf-8 -*-
import cargador_animales as c
def plumas_mas_piernas(animales:list)->str:
    mayor = 0
    nombremayor = None
    i = 0
    while i<len(animales):
        if animales[i]['feathers']== True and animales[i]['legs']> mayor:
            mayor = animales[i]['legs']
            nombremayor = animales[i]['animal_name']
        i +=1
    
    return nombremayor

lista = c.cargar_animales("zoo.csv")
nombre = plumas_mas_piernas(lista)
print("El animal con plumas y más patas es: " + nombre)