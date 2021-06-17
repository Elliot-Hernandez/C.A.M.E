#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 23:12:55 2021

@author: elliot
"""
from os import listdir
from os.path import isfile, join
from numpy import asarray
from numpy import savetxt
import numpy as np
import librosa, librosa.display
import matplotlib.pyplot as plt

path = '/home/elliot/Descargas/Sonidos_Tesis/Todos/'
files = [f for f in listdir(path) if isfile(join(path, f))]
files

def audio_rms_all(n, csv=False):
    for i in range(n):
        xd = path + files[i]
        x, sr = librosa.load(xd)
        rms = audio_rms(x, sr)
        if csv == True:
            csv = savetxt(files[i]+".csv", rms, delimiter=',')
            print('Se guardó el CSV del archivo ' + files[i])
        else:
            print('No se guardó el CSV del archivo ' + files[i])


# La duración del archivo:
# Ride-SessionDry-Stick-Mid-Soft.aif es = 10.8 s (888)

# files.index('Ride-SessionDry-Stick-Mid-Soft.aif')


"""
def audio_rms_index(n):
    xd = path + files[n]
    x, sr = librosa.load(xd)
    rms = audio_rms(x, sr)
    return(rms)
        
"""