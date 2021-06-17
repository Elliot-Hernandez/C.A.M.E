#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 19:29:12 2021

@author: elliot
"""
import librosa, librosa.display
import numpy as np
import matplotlib.pyplot as plt

def audio_rms(x, sr, hop_length, frame_length):
    hop_length = 256
    frame_length = 512

    energy = np.array([
    sum(abs(x[i:i+frame_length]**2))
    for i in range(0, len(x), hop_length)
    ])

    rms = librosa.feature.rms(x, frame_length=frame_length,
    hop_length=hop_length, center=True)
    rmse = rms[0]    
    return(rmse)