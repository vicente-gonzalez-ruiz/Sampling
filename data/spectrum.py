import sys
import numpy as np

x = np.loadtxt(window + ".dat")
y = np.abs(np.fft.rfft(x))

np.savetxt("spectrum" + window + ".dat", y)
