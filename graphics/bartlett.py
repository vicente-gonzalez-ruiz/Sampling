#!/usr/bin/env python

import numpy as np

x = np.concatenate((np.full(190, 0.0), np.bartlett(20)/10, np.full(190, 0.0)))

np.savetxt("bartlett.dat", x)
