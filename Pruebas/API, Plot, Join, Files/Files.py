#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 21:05:26 2021

@author: elliot
"""

from os import listdir
from os.path import isfile, join

files = [f for f in listdir('/home/elliot/Descargas/Sonidos_Tesis/Synthesis') if isfile(join('/home/elliot/Descargas/Sonidos_Tesis/Synthesis', f))]

files

