#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 12:32:20 2021

@author: elliot
"""
from os import listdir
from os.path import isfile, join
from numpy import asarray
from numpy import savetxt

import numpy, scipy, matplotlib.pyplot as plt, IPython.display as ipd
import librosa, librosa.display

import librosa, librosa.display
import numpy as np
import matplotlib.pyplot as plt

#path = ''
#files = [f for f in listdir(path) if isfile(join(path, f))]
#files

def audio_zcr_all(n):
    for i in range(n):
        xd = path + files[i]
        x, sr = librosa.load(xd)
        zcr = audio_zcr(x, sr)
        csv = savetxt(files[i]+".csv", zcr, delimiter=',')
        print('Se guardó el CSV del archivo ' + files[i])


"""
def audio_zcr_index(n):
    xd = path + files[n]
    x, sr = librosa.load(xd)
    zcr = audio_zcr(x, sr)
    return(zcr)

"""