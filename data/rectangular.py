import numpy as np

x = np.full(1000, 0.0)
x[1:999]=1.0
np.savetxt("rectangular.dat", x)
