import numpy as np
from numpy import genfromtxt

from scipy import signal
from sklearn.decomposition import FastICA, PCA
import csv

def fast_ica(brain, components):
    ica = FastICA(n_components=components)
    S_ = ica.fit_transform(brain)  # Reconstruct signals
    A_ = ica.mixing_  # Get estimated mixing matrix

    return S_

    # outfile = infile.split('.')[0] + 'fast_ica.csv'
    # with open(outfile, 'wb') as s:
    #     writer = csv.writer(s)
    #     writer.writerows(S_)

    # return outfile