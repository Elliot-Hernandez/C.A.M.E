#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Seleccionar carpeta para las descargas
import os
os.chdir(r"/home/elliot/Descargas/freesound-python/S")
------------------------------------------------------------------------
#Escoger aleatoriamente un archivo
import os, random
random.choice(os.listdir(r"/home/elliot/Descargas/freesound-python/S"))


------------------------------------------------------------------------
#Descargar sonidos de la API con "query" como buscador de tipos 
# de sonidos 
import freesound

client = freesound.FreesoundClient()
client.set_token(Key_API,"token")

results = client.text_search(query="hit",fields="id,name,previews")

for sound in results:
    sound.retrieve_preview(".",sound.name+".wav")
    print(sound.name)
    
    
results = client.text_search(query="hit",filter="duration:3",
                             fields="id,name,previews")
filter="channels:1"
    
------------------------------------------------------------------------
#superponer audios con otros audios
from pydub import AudioSegment
from pydub.playback import play

audio1 = AudioSegment.from_file("audio.mp3.wav")
audio2 = AudioSegment.from_file("audio")
audio3 = AudioSegment.from_file("audio") 

mixed = audio1.overlay(audio2)          
mixed1  = mixed.overlay(audio3)
mixed1.export("mixed.wav", format='wav') #exportar audio unido
play(mixed1)                             

#Escoger audio al azar de directorio
audio1 = AudioSegment.from_file(random.choice(os.listdir(r"/home/elliot/Descargas/freesound-python/S")))


-------------------------------------------------------------------------
#Pegar audios sin superponerlos
from pydub import AudioSegment
sound1 = AudioSegment.from_wav('C:/Users/Luis/Desktop/Elliot/UAML/UAM Clases/Proyecto Terminal/Primeros Ejercicios Python/Unir 2 sonidos/Glissando.wav')
sound2 = AudioSegment.from_wav('C:/Users/Luis/Desktop/Elliot/UAML/UAM Clases/Proyecto Terminal/Primeros Ejercicios Python/Unir 2 sonidos/HitR.wav')
combined_sounds = sound1 + sound2
combined_sounds.export(r"/home/elliot/Descargas/NombredelArchivo.wav", format="wav")
















