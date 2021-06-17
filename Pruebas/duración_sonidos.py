#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 21:50:37 2021

@author: elliot
"""
from os import listdir
from os.path import isfile, join
from numpy import asarray
from numpy import savetxt
import audioread

path = '/home/elliot/Descargas/Sonidos_Tesis/Todos/'
files = [f for f in listdir(path) if isfile(join(path, f))]
files


def audio_duration(n, dur=3000):
    for i in range(n):
        xd = path + files[i]
        with audioread.audio_open(xd) as f:
            totalsec = f.duration
            minn,secc = divmod(totalsec,60)
            if secc > dur:
                print("La duración del archivo " + files[i] + ' es = ' + str(secc))

