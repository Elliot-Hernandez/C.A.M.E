#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 23 21:59:46 2021

@author: elliot
"""
import numpy as np
import librosa, librosa.display
import matplotlib.pyplot as plt

from scipy.signal import hilbert
from scipy.signal import butter, filtfilt


#x, sr = librosa.load('/home/elliot/Descargas/Sonidos_Tesis/Transformed/camera.wav')
#librosa.display.waveplot(x, sr)

def hilbert_env(data,rolloff=0.0001):
    analytic_signal = hilbert(data)
    amp_env = np.abs(analytic_signal)
    amp_env = FilteredSignal(amp_env,rolloff)
    return amp_env
    

def FilteredSignal(signal, cutoff):
    B, A = butter(1, cutoff, btype='low')
    filtered_signal = filtfilt(B, A, signal, axis=0)
    return np.array(filtered_signal)


#xdd = hilbert_env(x, 0.0001)
#plt.plot(xdd)

#----------------------------------------------------------

#from numpy import asarray
#from numpy import savetxt
#savetxt('data.csv', xdd, delimiter=',')
"""
# SQL Base de datos 
# Servicios gratuitos de computación en nube (Amazon)
"""