# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 22:55:49 2024
Título: Gráficos más a detalle con matplotlib

Link para colores: https://htmlcolorcodes.com/es/

@author: eruiz1996
"""

# Módulos
import os
import matplotlib.pyplot as plt

# Working Directory
working_directory = r'C:\Users\ed_22\Documents\Python-AxM\Clase_08\Teoría'
os.chdir(working_directory)

# Módulos propios
from referencias import lenguajes, sueldos

plt.bar(lenguajes, sueldos)
#------------------------------------------------------------------------
# 3. Añadiendo colores
#plt.bar(lenguajes, sueldos, color='#229954')
#------------------------------------------------------------------------

#------------------------------------------------------------------------
# 4. Añadiendo otro gráfico
#plt.plot(lenguajes, sueldos, color='#B03A2E', 
#	linewidth=2, linestyle='--', marker='o')
#------------------------------------------------------------------------

#------------------------------------------------------------------------
# 1. Título
#plt.title('Lenguajes mejor pagados', fontsize=20)
#------------------------------------------------------------------------

#------------------------------------------------------------------------
# 2. Etiquetas para los ejes
#plt.xlabel('Lenguajes', fontsize=16)
#plt.ylabel('Miles de dólares', fontsize=16)
#------------------------------------------------------------------------
plt.show()