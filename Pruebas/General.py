#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 22:02:01 2021

@author: elliot
"""

#import energia as ene
#import ZeroCrossingRate as zc
#import onsets as ons
#import mel_mfcc as mel
#import mfcc as mfcc
import librosa, librosa.display
import matplotlib.pyplot as plt
import descriptores as desc

hop_length = 256
frame_length = 512

x, sr = librosa.load('/home/elliot/Documentos/Tésis/freesound-python/Sample 94 BPM.wav')
librosa.display.waveplot(x, sr)

# RMS
ene.audio_rms(x, sr, hop_length, frame_length)
rms = ene.audio_rms(x, sr, hop_length, frame_length)
rms

plt.plot(rms)

# ZCR
zc.audio_zcr(x, sr)
zcr = zc.audio_zcr(x, sr)
zcr

plt.plot(zcr)

#ON-SETS
ons.audio_onsets(x, sr)
onset_samples = ons.audio_onsets(x, sr)
onset_samples
#plt.plot(onset_samples)

#MFCC essentia
#frame_sz = 1024
#hop_sz = 500

mfcc.audio_mfcc(x, frame_sz, hop_sz)
mfcc = mfcc.audio_mfcc(x, frame_sz, hop_sz)

#MFCC LIBROSA
mel.audio_mfcc(x, sr)
mfcc = mel.audio_mfcc(x, sr)

plt.plot(mfcc)

#MEL-SPECTOGRAM
mel.audio_melspec(x, sr)
melspec = mel.audio_melspec(x, sr)

plt.plot(melspec)
---------------------------------------------------

import KClusters as kc

extract_features = kc.extract_features(x, sr)
features = kc.frame_size(x, sr, onset_samples)

import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import sklearn
min_max_scaler = sklearn.preprocessing.MinMaxScaler(feature_range=(-1, 1))
features_scaled = min_max_scaler.fit_transform(features)
plt.scatter(features_scaled[:,0], features_scaled[:,1])

kc.audio_cluster(n_clusters =  6, features_scaled = features_scaled)


