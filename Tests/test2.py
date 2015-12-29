#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import numpy as np
#import xray
import h5py
import dask.array as da
from dask.dot import dot_graph

filename = "/SNS/MANDI/IPTS-12697/0/4089/NeXus/MANDI_4089_histo.nxs"
f = h5py.File(filename,'r')


monitor = f['/entry/monitor1/data']
monitor_sum = monitor[:].sum()
print monitor_sum

banks = [5,5,11,12,13,17,18,19,20,21,22,27,28,29,31,32,33,37,39,40,41,42,47,48,49,50,51,52,58,59]

for bank in banks:
    dset = f['/entry/bank%s/data'%bank]
    x = da.from_array(dset, chunks=(16, 256, 3), lock=True)
    #c = x.dot(x)
    c = x.map_blocks(lambda x: x / monitor_sum)
    #c = x.sum()
    #dot_graph(c.dask)
    result = c.compute().mean().compute()
    print result
