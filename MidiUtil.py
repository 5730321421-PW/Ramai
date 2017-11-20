#!/usr/bin/env python

import random
import numpy

from midiutil.MidiFile import MIDIFile

degrees  = [60, 62, 64, 65, 67, 69, 71, 72] # MIDI note number
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
    MyMIDI.addNote(track, channel, pitch, time, duration, volume)
    time = time + 1

with open("random2.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)
