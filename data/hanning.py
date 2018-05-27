import numpy as np

x = np.hanning(1000)
np.savetxt("hanning.dat", x)
