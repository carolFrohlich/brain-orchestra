import numpy as np
from numpy import genfromtxt

#parse csv file
brain = genfromtxt('../data/rois2.csv', delimiter=',')

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

scale_tones = scale.minor_pentatonic(lowest_key - 12)
for i in scale_tones:
	if i >= 36:
		keys.append(i)

for i in xrange(lowest_key, 84, 12):
	scale_tones = scale.minor_pentatonic(i)
	for j in scale_tones:
		if j < 84:
			keys.append(j)



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



for i in range(len(ranged_brain[0])):	
	col = ranged_brain[:,i]
	
	for j in range(len(col)):
		num = col[j]
		#print num
		if num not in keys:#go up or down?
			down = True

			#if it's not the lasf
			if j <= len(col)-2:
				if col[j+1] >= num:
					down = False

			for k in range(len(keys)):
				if keys[k] > num:
					if down:
						col[j] = keys[k-1]
						print num, '->', keys[k-1]
						break
					else:
						col[j] = keys[k]
						print num, '->', keys[k]
						break




np.savetxt('../data/rois2__2.csv', ranged_brain, delimiter=",", fmt="%d")