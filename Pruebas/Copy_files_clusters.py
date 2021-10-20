#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 22:19:45 2021

@author: elliot
"""
#Copiar archivos basandose en las etiquetas

from os import listdir
from os.path import isfile, join

path = '/home/elliot/Descargas/Sonidos_Tesis/Todos/'
files = [f for f in listdir(path) if isfile(join(path, f))]




import cs
with open(, newline='') as f:
    reader = csv.reader(f)
    data = list(reader)
#print(data)



flattened  = [val for sublist in data for val in sublist]
#Limpiar las comillas '' "" del flattened
clean_n = [int(i) for i in flattened]



#Función para copiar los archivos basandose en su posición de la etiqueta del clúster
def copy_labels_cluster(clean_n):
    for i in clean_n:
        xd = path + files[i]
        src_path = xd 
        dst_path = r"/home/elliot/Descargas/Sonidos_Tesis/Sonidos_Etiquetados/Etiqueta_1/"
        shutil.copy(src_path, dst_path)
        #print('Copied')
        
        
"""
import shutil

src_path = r"/home/elliot/Descargas/Sonidos_Tesis/Todos/"+files[888] 
dst_path = r"/home/elliot/Descargas/Sonidos_Tesis/Sonidos_Etiquetados/Etiqueta_1/" + files[888]
shutil.copy(src_path, dst_path)
print('Copied')
"""
