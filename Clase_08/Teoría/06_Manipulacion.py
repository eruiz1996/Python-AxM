# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 23:59:11 2024
Título: Manipulación de DataFrames en Pandas

Descripción del problema:
Hacer un gráfico donde se muestre la evoluación histórica de la compañía
Tokio Marine respecto a su índice de Requerimiento de Capital de Solvencia

@author: eruiz1996
"""
import pandas as pd
import os

# definición del la ruta de lectura
read_dir = r'C:\Users\ed_22\Downloads'
file_name = 'IndicadoresAll.csv'
read_path = os.path.join(read_dir, file_name)
# lectura del archivo
df = pd.read_csv(read_path, sep=',', encoding='utf-8')
#%%
# leer cabeza
print(df.head())
print(df.head(10))
#%%
# nombres de columnas
print(df.columns)
#%%
# filtrar columnas (SELECT)
importantes = ['COMPANIA', 'Anio', 'Mes', 'Descripcion', 'importe1']
new_df = df[importantes]
print(new_df.head())
#%%
# renombrar columnas
# definimos diccionario (clave=orignales, valor=nuevos_nombres)
CAMPOS = {
    'COMPANIA':'nombre',
    'Anio':'ejercicio',
    'Mes':'trimestre',
    'Descripcion':'desc',
    'importe1':'importe'
}
new_df = new_df.rename(columns=CAMPOS)
#%%
# imprimimos información general
print(new_df.info())
#%%
# elementos únicos
new_df['trimestre'].unique()
#%%
# agregando una nueva columna
# hacemos minúsculas y tomamos los primeros tres caracteres
new_df['trim'] = new_df['trimestre'].str.lower().str[:3]
#%%
print(new_df.trim.head()) # otra manera de acceder
#%%
# sumando (concatenado) columnas
new_df['fecha'] = new_df['trim'].str.cat(new_df['ejercicio'].astype(str), sep='-')
new_df['fecha']
#%%
# quitamos columnas innecesarias
new_df.drop(columns=['ejercicio', 'trimestre', 'trim'], axis=1, inplace=True)
#%%
# filtrado booleano
filtro_tokio = new_df['nombre'] == 'Tokio Marine, Compañía de Seguros, S.A. de C.V.'
tokio_marine = new_df[filtro_tokio]
#%%
# filtrado con query
rcs = 'Indice de Cobertura de Requerimiento de Capital de Solvencia (Revisado por la CNSF)'
tokio_marine = tokio_marine.query("desc == @rcs").\
    drop(columns=['nombre', 'desc'], axis=1)
#%%
import matplotlib.pyplot as plt

tokio_marine.plot(
    x = 'fecha',
    y = 'importe',
    kind ='bar',
    rot = 45,
    title = 'RCS de Tokio Marine',
    color='#229954'
)
plt.tight_layout()
plt.show()