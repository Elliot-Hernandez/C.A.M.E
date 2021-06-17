#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  5 21:43:42 2021

@author: elliot
"""
# RMS

import librosa, librosa.display
import numpy as np
import matplotlib.pyplot as plt

def audio_rms(x, sr, hop_length=256, frame_length=512):
    energy = np.array([
    sum(abs(x[i:i+frame_length]**2))
    for i in range(0, len(x), hop_length)
    ])

    rms = librosa.feature.rms(x, frame_length=frame_length,
    hop_length=hop_length, center=True)
    rmse = rms[0]    
    return(rmse)

#-----------------------------------------------------------

# ON-SETS
import librosa

def audio_onsets(x, sr):
    onset_frames = librosa.onset.onset_detect(x, sr=sr, delta=0.04, wait=4)
    onset_times = librosa.frames_to_time(onset_frames, sr=sr)
    onset_samples = librosa.frames_to_samples(onset_frames)
    return(onset_samples)

#-----------------------------------------------------------

# ZCR

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

#-----------------------------------------------------------

# MFCC ESSENTIA

import librosa, librosa.display
import numpy, scipy, matplotlib.pyplot as plt, sklearn, librosa, urllib, IPython.display
import essentia, essentia.standard as ess


def audio_mfcc_e(x, frame_sz=1024, hop_sz=500):
    hamming_window = ess.Windowing(type='hamming')
    spectrum = ess.Spectrum()
    mfcc = ess.MFCC(numberCoefficients=13)

    mfccs = numpy.array([mfcc(spectrum(hamming_window(frame)))[1]
               for frame in ess.FrameGenerator(x, frameSize=frame_sz, hopSize=hop_sz)])
    
    mfccs = sklearn.preprocessing.scale(mfccs)
    plott = (plt.imshow(mfccs.T, origin='lower', aspect='auto',
 interpolation='nearest'), plt.ylabel('MFCC Coefficient Index'),
    plt.xlabel('Frame Index'))

    print(mfccs.shape)
    return(plott)

#-----------------------------------------------------------

#MELSPECTOGRAM

import librosa

def audio_melspec():
    melspec = librosa.feature.melspectrogram(y=x, sr=sr, n_mels=128, fmax=8000)
    #melspec = melspec[0]
    return(melspec)

#-----------------------------------------------------------

#MFCC LIBROSA
def audio_mfcc_l():
    mfcc = librosa.feature.mfcc(y=x, sr=sr)
    #mfcc = mfcc[0]
    return(mfcc)
#Usar los primeros 7

#-----------------------------------------------------------

#Spectral centroid

import numpy as np
import librosa, librosa.display
import matplotlib.pyplot as plt
import sklearn
import pandas as pd

def normalize(x, axis=0):
    return sklearn.preprocessing.minmax_scale(x, axis=axis)


def audio_spectral_centroid(x, sr):
    spectral_centroid = librosa.feature.spectral_centroid(x, sr=sr)[0]
    frames = range(len(spectral_centroid))
    t = librosa.frames_to_time(frames)

    spectral_centroid = librosa.feature.spectral_centroid(x+0.01, sr=sr)[0]
    return(spectral_centroid)
