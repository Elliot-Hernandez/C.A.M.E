#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 23:29:01 2021

@author: elliot
"""
import librosa

def audio_onsets(x, sr):
    onset_frames = librosa.onset.onset_detect(x, sr=sr, delta=0.04, wait=4)
    onset_times = librosa.frames_to_time(onset_frames, sr=sr)
    onset_samples = librosa.frames_to_samples(onset_frames)
    return(onset_samples)