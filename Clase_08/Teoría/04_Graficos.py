# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 22:55:49 2024
Título: Introducción a gráficos con matplotlib

@author: eruiz1996
"""

import os

# tomamos el directorio de trabajo
working_directory = r'C:\Users\ed_22\Documents\Python-AxM\Clase_08\Teoría'
# nos movemos a esa ruta
os.chdir(working_directory)
#%%
import matplotlib.pyplot as plt
# from matplotlib import pyplot as plt
from referencias import lenguajes, sueldos
#%%
plt.plot(lenguajes, sueldos)
plt.show()