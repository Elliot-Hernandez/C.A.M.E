#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 20:49:37 2021

@author: elliot
"""
import freesound

client = freesound.FreesoundClient()
client.set_token("wl5lr4l6pz4Hiuy41bF2da8HPXJdIwLmG34UX41t","token")

results = client.text_search(query="hit",filter="duration:3",
                             fields="id,name,previews")

for sound in results:
    sound.retrieve_preview(".",sound.name)
    print(sound.name)
    


#Otros
# results = client.text_search(query="hit",fields="id,name,previews")
# filter="channels:1"

#for sound in results: 
    #print(sound.name)
 
    #Tipos de Sonidos
#hit, granular, deep bass, delay, drone, convolution,
#synthesis, fm 

#Total 331 sonidos