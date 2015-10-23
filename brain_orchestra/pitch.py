import numpy as np
import pentatonic_scale as scale

def calculate_tone(brain):
	mean = np.mean(brain)
	tone = int((mean % 49) + 36)
	return tone

def calculate_lowest_key(tone):
	return (tone % 12) + 36

def generate_keys(scale, lowest_key):
	keys = []

	scale_tones = scale.minor_blues(lowest_key - 12)
	for i in scale_tones:
		if i >= 36:
			keys.append(i)

	for i in xrange(lowest_key, 85, 12):
		scale_tones = scale.minor_blues(i)
		for j in scale_tones:
			if j <= 84:
				keys.append(j)

	return keys


def generate_pitches(brain):
	#calculate brain tone, lowest and highest piano key
	tone = calculate_tone(brain)
	lowest_key = calculate_lowest_key(tone)

	print 'tone:', tone, 'lowest:' , lowest_key


	#generate all playable keys with selected scale
	keys = generate_keys(scale, lowest_key)
	print keys

	# x' = ((x - a) / (b - a)) * (b' - a') + a'
	def scale_column(column):
		return ((column - np.min(column)) / (np.max(column) - np.min(column))) * (keys[-1] - keys[0]) + keys[0]   


	ranged_brain = np.apply_along_axis(scale_column, 0, brain)
	ranged_brain = ranged_brain.astype(int)


	#fix matrix to contain only values from keys
	for i in range(len(ranged_brain[0])):	
		col = ranged_brain[:,i]
		
		for j in range(len(col)):
			if col[j] not in keys:
				col[j] = min(keys, key=lambda x:abs(x-col[j]))



	return ranged_brain