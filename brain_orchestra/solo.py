#load data
import numpy as np
from numpy import genfromtxt
from scipy.signal import argrelextrema


def allowed_endings(pitch):
    allowed = []
    allowed.append(pitch + 7)
    allowed.append(pitch - 5)
    lowest_pitch = (pitch % 12) + 36
    for i in xrange(lowest_pitch, 84, 12):
        allowed.append(i)
    return allowed


def fit_solo(brain, pitches, tempo, rois):

    for k in rois:
        #k = 140
        roi = brain[:,k]

        #find local minima
        min_index = argrelextrema(roi, np.less)[0]

        #try to map each phrase.
        # 1: Map each number to a piano key.
        # 2: adjust the last element of the phrase to be on the same tone as the first element
        ranged_roi = pitches[:,k]
        last = 0
        for i in min_index:
            phrase_tone_start = ranged_roi[last]
            phrase_tone_end = ranged_roi[i]

            right_pitches = allowed_endings(int(phrase_tone_start))
            if phrase_tone_end not in right_pitches:
                ranged_roi[i] = min(right_pitches, key=lambda x:abs(x-phrase_tone_end))

            last = i
            print 'start:', phrase_tone_start, 'end:', phrase_tone_end, 'right:', ranged_roi[i]
            print 'allowed pitches:', right_pitches
            print ''


        #adjust tempo of each phrase: phrases finish with whole note
        # 2: adjust the last element of the phrase to be on the same tone as the first element

        tempo_roi = tempo[:,k]
        for i in min_index:
            tempo_roi[i] = 1

    return pitches, tempo