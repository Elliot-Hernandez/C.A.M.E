#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 01:38:09 2021

@author: elliot
"""

from os import listdir
from os.path import isfile, join
from numpy import asarray
from numpy import savetxt
import numpy as np
import librosa, librosa.display
import matplotlib.pyplot as plt
import pandas as pd

path = '/home/elliot/Descargas/Sonidos_Tesis/Todos/'
files = [f for f in listdir(path) if isfile(join(path, f))]


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


def audio_rms_index(n, csv=False):
    xd = path + files[n]
    x, sr = librosa.load(xd)
    rms = audio_rms(x, sr)
    if csv == True:
        csv = savetxt(files[n]+".csv", rms, delimiter=',')
        print('Se guardó el CSV del archivo ' + files[n])
    else:
        print('No se guardó el CSV del archivo ' + files[n])
    return(rms)
    




i = 0 
while i < 29:
    series_list = [
    pd.Series(audio_rms_index(i)),
    ]
    i += 1
    print(i)
    result[i] = pd.concat(series_list, axis=1)    
    result.to_csv(path_or_buf='prueba2.csv',index=False)






aa = audio_rms_index(34)
s1 = pd.Series(aa)

aa2 = audio_rms_index(500)
s2 = pd.Series(aa2)

result = pd.concat([s1, s2], axis=1)
result.to_csv(path_or_buf='prueba1.csv',index=False)



series_list = [
pd.Series(audio_rms_index(0)),
pd.Series(audio_rms_index(1)),
pd.Series(audio_rms_index(2)),
pd.Series(audio_rms_index(3)),
pd.Series(audio_rms_index(4))
]

result = pd.concat(series_list, axis=1)    
result.to_csv(path_or_buf='prueba2.csv',index=False)




 