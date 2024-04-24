# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 23:11:46 2024
Título: Proceso de simulación Monte-Carlo

Instrucciones: 
    Calcula la probabilidad de que al lanzar un dado caiga un
    número par.

@author: eruiz1996
"""
#%%
# 1. Importamos módulos
import numpy as np
import matplotlib.pyplot as plt
#%%
# 2. Definimos parámetros
n = 100_000
simulaciones = []
exitos = 0
aproximaciones = []
#%%
# 3. Proceso de Simulación
for i in range(1, n + 1):
    # lanzamos el dado
    dado = np.random.choice(list(range(1, 7)))
    # en caso de caer par
    if dado % 2 == 0:
        # incrementamos un éxito
        exitos += 1
    # calcula la proporción de éxitos en la iteración actual
    aproximaciones.append(exitos / i)
#%%
# 4. Gráfica
# creamos índices para el eje x
indices = np.arange(1, n + 1, 1)
# graficamos las aproximaciones de las simulaciones
plt.plot(indices, aproximaciones)
# títulos
plt.xlabel('Número de simulaciones')
plt.ylabel('Probabilidad aproximada')
plt.title('Aproximación de la probabilidad de obtener un número par en un dado')
# línea de probabilidad real
plt.axhline(y=0.5, color='r', linestyle='--', label='Probabilidad real (0.5)')
plt.legend()
plt.show()