# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 18:47:51 2024
Título: Introducción a numpy

Cheat Sheet: 
    https://www.datacamp.com/cheat-sheet/numpy-cheat-sheet-data-analysis-in-python

@author: eruiz1996
"""
import numpy as np

numeros = list(range(1, 6))

arreglo = np.array(numeros)
#%%
# slicing
print(arreglo[:2])
#%%
# filtrado
filtro = arreglo > 3 # mask
print(filtro)
#%%
arreglo_filtrado = arreglo[filtro]
print(arreglo_filtrado)
#%%
# Matrices
matriz = [
    [1,2,3],
    [4,5,6]
]
matriz = np.array(matriz)
#%%
# atributo shape
print(matriz.shape)
#%%
# slicing en matrices
# elemento (0,0)
primer_ele = matriz[0, 0]
print(primer_ele)
#%%
# primer columna
primer_col = matriz[:, 0]
print(primer_col)
#%%
# úlitma columna
ult_col = matriz[:, -1]
print(ult_col)
#%%
# primer renglón
primer_ren = matriz[0, :]
print(primer_ren)
#%%
# matriz traspuesta
print(matriz.T)
#%%
# Matrices especiales
# 1. Identidad
identidad = np.eye(3)
print(identidad)
#%%
# matriz de ceros
ceros = np.zeros(matriz.shape)
print(ceros)
#%%
# matriz de unos
unos = np.ones((2, 3))
print(unos)
#%%
# VECTORIZACIÓN
a = np.ones(3)
b = np.array([-1, 2, 9])
# suma
print(a + b)
#%%
# resta
print(a - b)
# multiplicación
print(a * b)
# división
print(a / b)
#%%
# con matrices
print(matriz * matriz.T)
# el operador * hace multiplicación elemento a elemento
#%%
resultado = np.matmul(matriz, matriz.T)
print(resultado)
otra_manera = matriz @ matriz.T
print(otra_manera)
#%%
# producto punto
producto_punto = a.dot(b)
print(producto_punto)
#%%
# random en numpy
np.random.seed(9)
volado = np.random.choice(['Águila', 'Sol'])
print(volado)
#%%
# vectorización con funciones
cuadrados = [n**2 for n in range(1, 11)]
cuadrados = np.array(cuadrados)
raices = np.sqrt(cuadrados) # sí, math también está en numpy
#%%
# funciones de acumulación
suma_unos = unos.sum()
print(suma_unos) # ver matriz 'unos'