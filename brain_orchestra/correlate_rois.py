import numpy as np
from numpy import genfromtxt


brain = genfromtxt('../data/filt_global_OHSU_0050142_rois_cc200.1D', delimiter='\t')
corr_matrix  = np.corrcoef(brain, rowvar=0)

np.fill_diagonal(corr_matrix, 100.0)
corr_matrix = np.tril(corr_matrix)


print np.min(corr_matrix)
print np.max(corr_matrix)



#indices = np.where(corr_matrix >= -0.01) and np.where(corr_matrix <= 0.01)
indices = np.where(corr_matrix <= -0.8)
print len(indices[0])

for i in range(len(indices[0])):
    if indices[0][i] > indices[1][i]:
        print indices[0][i], indices[1][i], corr_matrix[indices[0][i]][indices[1][i]]



# from pylab import *
# A = rand(200,200)
# figure(1)
# imshow(corr_matrix, interpolation='nearest')
# colorbar()
# grid(True)
# show()