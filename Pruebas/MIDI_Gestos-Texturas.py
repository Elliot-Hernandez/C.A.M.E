# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 19:47:50 2021

@author: Elliot
"""

import random 
import time
import rtmidi

midiout = rtmidi.MidiOut()
available_ports = midiout.get_ports()

print(available_ports)

if available_ports:
    midiout.open_port(1)
else:
    midiout.open_virtual_port("My virtual output")


count_1 = 1
while count_1 <= 10:
    
    n = random.randint(0,6)
    note_on = [0x90, n, 112]
    note_off = [0x80, n, 0]
    midiout.send_message(note_on)
    time.sleep(0)
    midiout.send_message(note_off)
    
    print(count_1)
    count_1 += 1

