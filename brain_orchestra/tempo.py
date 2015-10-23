import numpy as np
import copy

def generate_tempo(brain, tempo_notes=[1,2,4,8]):

    #generate tempo file
    tempos = np.ones(brain.shape)
    #tempos = tempos.fill(tempo_notes[-1])
    tempos2 = np.ones((len(brain), 1))


    for i in range(brain.shape[1]):

        smallest_jump_index = []
        bigest_jump_index = []
        min_difference = 10000.0
        max_difference = -10000.0

        col = brain[:,i]
        for j in range(len(col)-1):
            num1 = col[j]
            num2 = col[j + 1]

            #find smallest jump
            dif = np.abs(num1 - num2)
            if dif < min_difference:
                min_difference = dif
                smallest_jump_index = [j, j+1]

            #find biggest jump
            if dif > max_difference:
                max_difference = dif
                bigest_jump_index = [j, j+1]


        #now we have the max and min jump, let's calculate the intermediate values (1/2, 1/4)
        ranges = []
        num_ranges = len(tempo_notes)
        step = (min_difference + max_difference) / float(num_ranges)

        range_min = min_difference
        range_max = min_difference + step

        for i in range(num_ranges):
            new_range = [range_min,range_max]
            ranges.append(new_range)
            range_min = range_max
            range_max = range_max + step


        #iterate over the column again and transform each jump in a tempo
        col = brain[:,i]
        for j in range(len(col)-1):
            num1 = col[j]
            num2 = col[j + 1]
            dif = np.abs(num1 - num2)

            #usar var range em vez de whole, half, quarter.....
            for ridx,r in enumerate(ranges):
                if r[0] <= dif < r[1]:
                    tempos[j,i] = tempo_notes[ridx]


        tempos2 = np.c_[tempos2, tempos[:,i]]


    tempos2 = np.delete(tempos2, 0, axis=1)
    tempos2[tempos2.shape[0]-1, :] = tempos2[tempos2.shape[0]-2, :]

    return tempos2
