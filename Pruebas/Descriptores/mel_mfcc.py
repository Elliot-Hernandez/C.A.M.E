#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 17:58:02 2021

@author: elliot
"""
import librosa

#Melspectogram
def audio_melspec(x, sr):
    melspec = librosa.feature.melspectrogram(y=x, sr=sr, n_mels=128, fmax=8000)
    #melspec = melspec[0]
    return(melspec)

#MFCC
def audio_mfcc(x, sr):
    mfcc = librosa.feature.mfcc(y=x, sr=sr)
    #mfcc = mfcc[0]
    return(mfcc)
#Usar los primeros 7
