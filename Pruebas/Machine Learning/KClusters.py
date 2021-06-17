#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 12:20:23 2021

@author: elliot
"""
import numpy as np
import matplotlib.pyplot as plt
import librosa
import numpy, scipy, matplotlib.pyplot as plt, IPython.display as ipd
import librosa, librosa.display
from sklearn.preprocessing import MinMaxScaler
import sklearn


def extract_features(x, fs):
    zcr = librosa.zero_crossings(x).sum()
    energy = scipy.linalg.norm(x)
    return [zcr, energy]


def frame_size(x, sr, onset_samples):
    frame_sz = sr*0.1
    f_sz = int(frame_sz)
    features = np.array([extract_features(x[i:i+f_sz], sr) for i in onset_samples])
    return(features)
    

#min_max_scaler = sklearn.preprocessing.MinMaxScaler(feature_range=(-1, 1))
#features_scaled = min_max_scaler.fit_transform(features)
#plt.scatter(features_scaled[:,0], features_scaled[:,1])


#-------------------------
def audio_cluster(n_clusters, features_scaled):
    n_clusters = n_clusters
    model = sklearn.cluster.KMeans(n_clusters)
    labels = model.fit_predict(features_scaled)
    
    pllot=plt.scatter(features_scaled[labels==0,0], features_scaled[labels==0,1], c='r')
    pllot=plt.scatter(features_scaled[labels==1,0], features_scaled[labels==1,1], c='g')
    pllot=plt.scatter(features_scaled[labels==2,0], features_scaled[labels==2,1], c='b')
    pllot=plt.scatter(features_scaled[labels==3,0], features_scaled[labels==3,1], c='y')
    pllot=plt.scatter(features_scaled[labels==4,0], features_scaled[labels==4,1], c='cyan')
    pllot=plt.scatter(features_scaled[labels==5,0], features_scaled[labels==5,1], c='orange')
    pllot=plt.scatter(features_scaled[labels==6,0], features_scaled[labels==6,1], c='black')
    pllot=plt.scatter(features_scaled[labels==7,0], features_scaled[labels==7,1], c='#bf8c00')
    pllot=plt.scatter(features_scaled[labels==8,0], features_scaled[labels==8,1], c='#a2ff00')
    return(model, labels)
    print(pllot)