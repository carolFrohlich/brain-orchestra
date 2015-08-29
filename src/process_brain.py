import numpy as np
from numpy import genfromtxt

#parse csv file
brain = genfromtxt('../data/rois5.csv', delimiter=',')

#calculate brain tone, lowest and highest piano key
mean = np.mean(brain)
tone = int((mean % 49) + 36)
lowest_key = (tone % 12) + 36

highest_key = lowest_key + 48
if highest_key > 84:
	highest_key -= 12


print 'tone:', tone, 'lowest:' , lowest_key, 'highest:', highest_key


#generate all playable keys with selected scale
import pentatonic_scale as scale

keys = []

for i in xrange(lowest_key,highest_key, 12):
	scale_tones = scale.minor_pentatonic(i)
	keys.extend(scale_tones)


print keys


# make sure all brain values are mapped to one of the key values
# I don't know the best way to do this :(
# Approach 1:
# Scale brain numbers between min(keys) and max(keys)
# foreach number, if number not in keys, transform it into the nearest keys 


# x' = ((x - a) / (b - a)) * (b' - a') + a'



def x(column):
	return ((column - np.min(column)) / (np.max(column) - np.min(column))) * (keys[-1] - keys[0]) + keys[0]


ranged_brain = np.apply_along_axis(x, 0, brain)


ranged_brain = ranged_brain.astype(int)


def adjust_number(num):
	if num in keys:
		return num
	else:
		for i in range(len(keys)):
			if keys[i] > num:
				return keys[i-1]



vector_func = np.vectorize(adjust_number)
scaled_brain = vector_func(ranged_brain)


np.savetxt('../data/rois5_minor_pentatonic.csv', scaled_brain, delimiter=",", fmt="%d")