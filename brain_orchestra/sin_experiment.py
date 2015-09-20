import numpy as np
# from numpy import genfromtxt

# #parse csv file
# brain = genfromtxt('../data/rois2.csv', delimiter=',')


t = np.arange(0.0, 2.36, 0.01)
print t.shape
sin_wave1 = [np.sin(2*np.pi*x) for x in t]
sin_wave2 = [np.sin(-2*np.pi*x) for x in t]


from pylab import figure, show
fig = figure(1)
ax1 = fig.add_subplot(211)
ax1.plot(sin_wave1)
ax1.plot(sin_wave2)
show()



# for i in range(brain.shape[1]):
#     col = brain[:,i]
#     sin_wave = [np.sin(x) for x in range(i, 236 + i)]
#     for j,val in enumerate(col):
#         col[j] = col[j]*sin_wave[j]



# np.savetxt('../data/rois2_sine.csv', brain, delimiter=",", fmt="%d")