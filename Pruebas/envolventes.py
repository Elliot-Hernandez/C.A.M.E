#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 25 11:55:49 2021

@author: elliot
"""
from os import listdir
from os.path import isfile, join
from numpy import asarray
from numpy import savetxt

path = ''
files = [f for f in listdir(path) if isfile(join(path, f))]
files


def audio_env(n, rolloff=0.005, csv=False):
    n = n
    xd = path + files[n]
    x, sr = librosa.load(xd)
    dos = hilbert_env(x, rolloff)
    if csv == True:
        csv = savetxt(files[n]+".csv", dos, delimiter=',')
        print('Se guardó el CSV del archivo ' + files[n])
    else:
        print('No se guardó el CSV del archivo ' + files[n])
    graf = plt.plot(dos)
    print(graf, dos)
    

"""
Cargar todos los archivos, graficar y guardar archivos CSV

def prueba(n, rolloff=0.005):
    for i in range(n):
        xd = path + files[i]
        x, sr = librosa.load(xd)
        dos = hilbert_env(x, rolloff)
        csv = savetxt(files[i]+".csv", dos, delimiter=',')
        print('Se guardó el CSV del archivo ' + files[i])
        graf = plt.plot(dos)
        print(graf)
    
-----------------------------------------------------

def audio_env_all(n, rolloff=0.005):
    for i in range(n):
        xd = path + files[i]
        x, sr = librosa.load(xd)
        dos = hilbert_env(x, rolloff)
        csv = savetxt(files[i]+".csv", dos, delimiter=',')
        print('Se guardó el CSV del archivo ' + files[i])
    #graf = plt.plot(dos) 
    #graf = plt.savefig('/home/elliot/Documentos/Tésis/freesound-python/C.A.M.E/Plots/Prueba/' + files[i] + '.png')
    #print(graf)
        
"""