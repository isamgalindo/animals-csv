# Animals csv

<a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> 

## Table of contents
* [Introduction](#Introduction)
* [How to run it](#Run)
* [Additional things](#Characteristics)

### Introduction
Python console with a menu of options to interact with. 

### Run
1. Make sure you have python installed in your computer
```
python3 --version
```
- If you don´t have it, run the following lines in your terminal (Mac):
* If you don´t have homebrew installed, run this:
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
* Install pythn using homebew:
```
 brew install python
```
* Verify the version
```
python3 --version
```
  
2. Run cargador_animales.py file. It will upload a csv of that has animals and some characteristics.
3. Then, run any of the other files to interact with the csv
https://github.com/isamgalindo/animals-csv/blob/0119bf79cb3d6883d321d997f4de3cc92b66909c/actividad_lab1.py
![image](https://github.com/isamgalindo/animals-csv/assets/141882033/6e14126e-dc98-474c-b736-635aa37734e9)
![image](https://github.com/isamgalindo/animals-csv/assets/141882033/3c904932-3cd7-4387-9f96-c4072a20fe86)

```
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
```

### Characteristics
- genero (genre) is either F (femenino) or M (masculino)
- peso (weight) is in kg
- tipo de sangre (blood type) could be A+, A-, AB+, AB-, B+, B-, O+, O-



