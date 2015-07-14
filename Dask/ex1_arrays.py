#!/usr/bin/env python
# -*- coding: utf-8 -*-

import dask.array as da
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from dask.dot import dot_graph

# Random 3D array (drop-in NumPy replacement)
x = da.random.normal(10, 0.1, size=(50, 50, 50), chunks=(25, 25, 25))
x.dask

# Squash to 2D (DO not compute!)
mean = x.mean(axis=0)
mean.dask

# See the plot!
dot_graph(mean.dask)
res = mean.compute()

print res.shape

plt.figure()
image = mpimg.imread("mydask.png")
plt.imshow(image)

plt.figure()
plt.imshow(res)
plt.show()
