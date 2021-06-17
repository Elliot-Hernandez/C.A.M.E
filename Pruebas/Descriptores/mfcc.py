#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 20:57:22 2021

@author: elliot
"""
import librosa, librosa.display
import numpy, scipy, matplotlib.pyplot as plt, sklearn, librosa, urllib, IPython.display
import essentia, essentia.standard as ess


def audio_mfcc(x, frame_sz, hop_sz):
    hamming_window = ess.Windowing(type='hamming')
    spectrum = ess.Spectrum()
    mfcc = ess.MFCC(numberCoefficients=13)
    frame_sz = 1024
    hop_sz = 500

    mfccs = numpy.array([mfcc(spectrum(hamming_window(frame)))[1]
               for frame in ess.FrameGenerator(x, frameSize=frame_sz, hopSize=hop_sz)])
    
    mfccs = sklearn.preprocessing.scale(mfccs)
    plott = (plt.imshow(mfccs.T, origin='lower', aspect='auto',
 interpolation='nearest'), plt.ylabel('MFCC Coefficient Index'),
    plt.xlabel('Frame Index'))

    print(mfccs.shape)
    return(plott)
