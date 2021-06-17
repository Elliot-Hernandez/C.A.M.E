#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

def unir_sonidos(audio1, audio2):    
    out = audio1 + audio2
    path = out.export(r"/home/elliot/Descargas/prueba.wav", format="wav")
    print ("Directorio de salida %s" % path)
    return out