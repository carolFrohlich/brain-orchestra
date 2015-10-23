from numpy import genfromtxt
import numpy as np

import pitch
import tempo
import midi

import solo

brain = genfromtxt('../data/func_minimal_OHSU_0050142.1D', delimiter='\t')
brain = brain[1:]
print len(brain)



pitches = pitch.generate_pitches(brain)
tempos = tempo.generate_tempo(brain, [1,2,4,8])
tempos_nowhole = tempo.generate_tempo(brain, [2,4,8])


solo_rois = [41]
for s in solo_rois:
    tempos[:,s] = tempos_nowhole[:,s]

pitches, tempos = solo.fit_solo(brain, pitches, tempos, solo_rois)





midi.save_midi(pitches, tempos, [{'id':121,'instrument':42, 'solo':True}], '../midi/func_minimal.mid')





#http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0049773`
