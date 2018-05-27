import numpy as np

x = np.bartlett(1000)
np.savetxt("bartlett.dat", x)
