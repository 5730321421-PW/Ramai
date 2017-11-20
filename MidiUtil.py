#!/usr/bin/env python

import random
import numpy

from midiutil.MidiFile import MIDIFile

degrees  = [60, 62, 64, 65, 67, 69, 71, 72] # MIDI note number
length = [0.25,0.5,0.75,1,1.5,2,3,4]
track    = 0
channel  = 0
time     = 0   # In beats
duration = 1   # In beats
tempo    = 60  # In BPM
volume   = 100 # 0-127, as per the MIDI standard
scaleShift = 2

MyMIDI = MIDIFile(1) # One track, defaults to format 1 (tempo track
                     # automatically created)
MyMIDI.addTempo(track,time, tempo)

degreePy = numpy.array(degrees)
scale = degreePy+scaleShift

for i in range(19):
    pitch = random.choice(scale)
    duration = random.choice(length)
    MyMIDI.addNote(track, channel, pitch, duration, duration, volume)
    time = time + duration

with open("random3.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)
