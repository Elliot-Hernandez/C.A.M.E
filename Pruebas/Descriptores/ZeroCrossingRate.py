#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 20:35:59 2021

@author: elliot
"""

import numpy, scipy, matplotlib.pyplot as plt, IPython.display as ipd
import librosa, librosa.display

def audio_zcr(x, sr):
    ipd.Audio(x, rate=sr)
    n0 = 6500
    n1 = 7500
    zero_crossings = librosa.zero_crossings(x[n0:n1], pad=False)
    zcrs = librosa.feature.zero_crossing_rate(x)
    zcr = zcrs[0]
    return(zcr)