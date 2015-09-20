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

	scale_tones = scale.minor_pentatonic(lowest_key - 12)
	for i in scale_tones:
		if i >= 36:
			keys.append(i)

	for i in xrange(lowest_key, 85, 12):
		scale_tones = scale.minor_pentatonic(i)
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
						else:
							col[j] = keys[k]


	return ranged_brain