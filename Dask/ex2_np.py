import dask.array as da
import numpy as np
import time

def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        print 'Time: %2.6f sec' % (te-ts)
        return result
    return timed

def task(arr):
    #return arr.std(axis=1)
    return arr.dot(arr)

@timeit
def task_np(arr):
    return task(arr)

@timeit
def task_da(arr):
    arr = task(arr)
    return arr.compute()

N = 80

np_arr = np.random.random_sample(size=(N,N,N))

da_arr = da.from_array(np_arr, chunks=(100, 100, 100))
#da_arr = da.random.normal(73, 1, size=(N,N), chunks=(10000))

print 30*'-', "Numpy", 30*'-'
np_arr = task_np(np_arr)
print 30*'-', "Dask", 30*'-'
da_arr = task_da(da_arr)
