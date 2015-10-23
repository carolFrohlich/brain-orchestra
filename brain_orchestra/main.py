from numpy import genfromtxt
import numpy as np

import pitch
import tempo
import midi
import solo
import choose_rois


brain = genfromtxt('../data/filt_global_OHSU_0050142_rois_cc200.1D', delimiter='\t')
brain = choose_rois.fast_ica(brain, 3)


pitches = pitch.generate_pitches(brain)
tempos = tempo.generate_tempo(brain, [1,2,4,8,16])
tempos_nowhole = tempo.generate_tempo(brain, [2,4,8])


solo_rois = [0]
for s in solo_rois:
    tempos[:,s] = tempos_nowhole[:,s]

pitches, tempos = solo.fit_solo(brain, pitches, tempos, solo_rois)


instruments = [{'id':0,'instrument':1, 'solo':True},
    {'id':1,'instrument':33, 'solo':False},
    # {'id':2,'instrument':14, 'solo':False}
    ]

midi.save_midi(pitches, tempos, instruments, '../midi/test3.mid')




#TODO: learn how to use sound fonts
#TODO: COMMENTS 
#http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0049773