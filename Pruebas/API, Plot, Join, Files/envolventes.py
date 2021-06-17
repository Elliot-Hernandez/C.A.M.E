#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 17 17:43:33 2021

@author: elliot
"""

import numpy as np
import librosa
W, _ = librosa.load("/home/elliot/Descargas/Sonidos_Tesis/Synthesis/HMS_6.wav")
X_pos_frontier, X_neg_frontier = se.get_frontiers(W, 0)
#print(X_pos_frontier, W[X_pos_frontier])

plt.plot(X_pos_frontier, W[X_pos_frontier])

-------------------------------


#Crear envolvente
import numpy as np
from scipy.interpolate import interp1d
import signal_envelope as se 

np.random.seed(0)
n = 100
X = np.arange(n)

f = interp1d([0, 0.25 * n, 0.5 * n, 0.75 * n, n], np.abs(2 + np.random.normal(0, .3, 5)), "cubic")
E_original = f(X)

plt.plot(E_original)

#Envolvente de Hillbert