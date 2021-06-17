#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 12:02:16 2021

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

path = '/home/elliot/Documentos/Tésis/freesound-python/C.A.M.E/CSV_ZCR/ZCR_no_0/'
files = [f for f in listdir(path) if isfile(join(path, f))]
files


def zero_list(n):
    zeros = [0] * n
    return(zeros)


def audio_csv_0(n):
    for i in range(n):
        xd = path + files[i]
        df = pd.read_csv(xd)
        df1 = pd.DataFrame(df)
        fill = pd.DataFrame(zero_list(937-len(df1)))
        frames = [df1, fill]
        r = pd.concat(frames, ignore_index=True).fillna(0)
        r.to_csv(path_or_buf=files[i],index=False)
        

"""
----------------------------------------------------------------
df1 = pd.DataFrame(audio_csv_path(0))

fill = pd.DataFrame(zero_list(936-78))
frames = [df1, fill]
r = pd.concat(frames, ignore_index=True).fillna(0)
----------------------------------------------------------------
----------------------------------------------------------------

def audio_csv_0_index(n, csv=False):
    xd = path + files[n]
    df = pd.read_csv(xd)
    if csv == True:
        csv = savetxt(files[n]+".csv", rms, delimiter=',')
        print('Se guardó el CSV del archivo ' + files[n])
    else:
        print('No se guardó el CSV del archivo ' + files[n])
    return(df)

----------------------------------------------------------------
----------------------------------------------------------------

for i in range(len(files)):
    df1 = pd.DataFrame(audio_csv_0_index(i))
    print(df1.shape)

----------------------------------------------------------------
"""

