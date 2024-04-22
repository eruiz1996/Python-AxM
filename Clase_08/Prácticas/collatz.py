# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 21:03:11 2024
Título: Conjetura de Collatz

Instrucciones: 
    Hacer una gráfica de puntos con todos los números por los que pasa un
    número hasta cumplir la conjetura de Collatz

@author: eruiz1996
"""
# 1. Importamos módulos
import numpy as np
import matplotlib.pyplot as plt
#%%
# 2. Definimos función para aplicar algoritmo de Collatz
def collatz(n):
    # si el número es par
    if n % 2 == 0:
        return n/2
    else:
        return 3*n+1
#%%
# 3. Pedimos el n al usuario
n = int(input('Introduce un número entero positivo: '))
#%%
# 4. Ejecutamos código de manera recursiva
pasos = []
while n != 1:
    n = collatz(n)
    pasos.append(n)
#%%
# 5. Graficamos
indices = np.arange(1, len(pasos) + 1)
plt.scatter(indices, pasos, label = f'{len(pasos)} pasos')
# títulos
plt.xlabel('Número de pasos')
plt.ylabel('Valor obtenido')
plt.title('Conjetura de Collatz')
plt.legend()
plt.grid(True)
plt.show()