# -*- coding: utf-8 -*-
import cargador_animales as c

def contar_animales_con_plumas(animales:list)->int:
    cantidad = 0
    i = 0
    while i< len(animales):
        if animales[i]['feathers']== True:
            cantidad += 1
        i+=1
          
    return cantidad

lista = c.cargar_animales("zoo.csv")
cantidad = contar_animales_con_plumas(lista)
print("Hay " + str(cantidad) + " animales con plumas.")