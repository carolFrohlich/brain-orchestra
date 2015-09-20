from numpy import genfromtxt
import numpy as np

import pitch
import tempo
import midi

import solo

brain = genfromtxt('../data/rois2.csv', delimiter=',')

pitches = pitch.generate_pitches(brain)
tempos = tempo.generate_tempo(brain, [1,2,4,8])
tempos_nowhole = tempo.generate_tempo(brain, [2,4,8])


solo_rois = [80]
for s in solo_rois:
    tempos[:,s] = tempos_nowhole[:,s]

pitches, tempos = solo.fit_solo(brain, pitches, tempos, solo_rois)


midi.save_midi(pitches, tempos, [141,146,96,80], '../midi/test6.mid')





#http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0049773`
