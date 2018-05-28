#!/usr/bin/env python

import numpy as np

x = np.full(400, 0.0)
x[190:210]=1/20

np.savetxt("rectangular.dat", x)
