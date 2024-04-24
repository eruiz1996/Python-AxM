# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 18:05:47 2024
Título: Entiendo a Spyder

Temas:
    - módulo os
    - módulo random
    - módulo math

Documentación Oficial:
    - os: https://docs.python.org/es/3.10/library/os.html
    - random: https://docs.python.org/es/3/library/random.html
    - math: https://docs.python.org/3/library/math.html
@author: eruiz1996
"""
#%% 
import os
#%%
print('Hola Mundo')
#%%
print('Adiós Mundo')
for i in range(5):
    print(i)
#%%
# working directory
working_dir = r'C:\Users\ed_22\Documents\Python-AxM\Clase_08\Teoría'
#%%
# PATHS y DIRECTORIOS

os.chdir(working_dir)
#%%
documentos = os.listdir()
#%%
otro_path = os.listdir(r'C:\Users\ed_22\Documents\Python-AxM\Clase_08\Prácticas')
#%%
archivo = 'ejemplo.xlsx'
ruta_archivo = os.path.join(working_dir, archivo)
print(ruta_archivo)
#%%
import random
#%%
random.seed(12)
print(random.random())
#%%
random.seed(12000)
numeros = list(range(10, 21))
print(random.choice(numeros))
#%%
a, b = 2, 8
print(random.randint(a, b))
#%%
from math import pi, e, sqrt
#%%
print(sqrt(100))