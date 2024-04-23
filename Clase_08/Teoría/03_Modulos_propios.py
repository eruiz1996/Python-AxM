# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 21:49:45 2024
Título: Importar módulos propios

@author: eruiz1996
"""
import os

# tomamos el directorio de trabajo
working_directory = r'C:\Users\ed_22\Documents\Python-AxM\Clase_08\Teoría'
# nos movemos a esa ruta
os.chdir(working_directory)
#%%
# Importando objetos
from referencias import PIB
print(PIB)
#%%
from referencias import lenguajes, sueldos
print(lenguajes)
print(sueldos)
#%%
# Las funciones también son objetos
from referencias import crear_diccionario
mejor_pagados = crear_diccionario(lenguajes, 'Lenguajes', sueldos, 'Sueldos')
print(mejor_pagados)
#%%
"""
Si se quiere importar todo lo que hay dentro de un módulo se debe de usar:
    
    from nombre_modulo import *
    
Pero esto es una mala práctica, nunca hacerlo
"""