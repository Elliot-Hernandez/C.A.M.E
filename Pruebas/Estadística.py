#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 13:33:36 2021

@author: elliot
"""
import pandas as pd
from os import listdir
from os.path import isfile, join
from numpy import asarray
from numpy import savetxt

# MEDIA

path = ''
files = [f for f in listdir(path) if isfile(join(path, f))]
files


def audio_mean_all(n):
    for i in range(n):
        xd = path + files[i]
        df = pd.read_csv(xd)
        media = df.mean()
        return(media)
        #print(media)
        #csv = savetxt(files[i]+".csv", media, delimiter=',')
        #print('Se guardó el CSV del archivo ' + files[i])
        

"""
df = pd.read_csv("/home/elliot/Documentos/Tésis/freesound-python/C.A.M.E/CSV_Envolventes/Bass/ahj-subdrop-maxbass.wav.csv")
media = df.mean()
print(media)
"""
#-------------------------------------------------------------

# DESVIACIÓN ESTÁNDAR

def audio_std_all(n):
    for i in range(n):
        xd = path + files[i]
        df = pd.read_csv(xd)
        d_std = df.std()
        return(d_std)
        #print(d_std)
        #csv = savetxt(files[i]+".csv", d_std, delimiter=',')
        #print('Se guardó el CSV del archivo ' + files[i])

#-------------------------------------------------------------


def audio_rms_mean_index(n):
    xd = path + files[n]
    x, sr = librosa.load(xd)
    rms = audio_rms(x, sr)
    rmse = rms.mean()
    return(rmse)

def audio_rms_d_std_index(n):
    xd = path + files[n]
    x, sr = librosa.load(xd)
    rms = audio_rms(x, sr)
    rmse = rms.std()
    return(rmse)

------------------------------

def audio_zcr_mean_index(n):
    xd = path + files[n]
    x, sr = librosa.load(xd)
    zcr = audio_zcr(x, sr)
    zcrr = zcr.mean()
    return(zcrr)

def audio_zcr_d_std_index(n):
    xd = path + files[n]
    x, sr = librosa.load(xd)
    zcr = audio_zcr(x, sr)
    zcrr = zcr.std()
    return(zcrr)

------------------------------

def audio_spectral_centroid_mean_index(n):
    xd = path + files[n]
    x, sr = librosa.load(xd)
    spc = audio_spectral_centroid(x, sr)
    spc_cnt = spc.mean()
    return(spc_cnt)

def audio_spectral_centroid_d_std_index(n):
    xd = path + files[n]
    x, sr = librosa.load(xd)
    spc = audio_spectral_centroid(x, sr)
    spc_cnt = spc.std()
    return(spc_cnt)
