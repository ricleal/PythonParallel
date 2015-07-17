import numpy as np
import time
from distarray.globalapi import Context
import distarray.globalapi as da

'''
Needs IPython da cluster running:
dacluster start -n4
'''

def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        print 'Time: %2.6f sec' % (te-ts)
        return result
    return timed

context = Context()



@timeit
def task_np(arr):
    return (np.sin(arr) + np.cos(arr)).sum(axis=1) / arr.sum(axis=2)

@timeit
def task_da(arr):
    return (da.sin(arr) + da.cos(arr)).sum(axis=1) / arr.sum(axis=2)

N = 400

np_arr = np.random.random_sample(size=(N,N,N))

da_arr = context.fromarray(np_arr)

#da_arr = da.random.normal(73, 1, size=(N,N), chunks=(10000))

print 30*'-', "Numpy", 30*'-'
np_arr = task_np(np_arr)
print 30*'-', "DistArray", 30*'-'
da_arr = task_da(da_arr)
