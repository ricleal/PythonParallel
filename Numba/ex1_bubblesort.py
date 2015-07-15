import numpy as np
from numba import jit

"""
demonstrate compiled extensions using bubblesort
"""

def bubblesort(items):
    ''' Regular bubblesort '''
    length = len(items)
    swapped = 1
    for i in range(0, length):
        if swapped:
            swapped = 0
            for ele in range(0, length-i-1):
                if items[ele] > items[ele + 1]:
                    temp = items[ele + 1]
                    items[ele + 1] = items[ele]
                    items[ele] = temp
                    swapped = 1
    return items

# Add jit to regular bubblesort
# A decorator on the fucntion could also be used: @jit
jitbubblesort = jit(bubblesort)

import time
for N in (100,100,1000,1000,10000):

    randoms = np.random.randint(0,1000,(N)).tolist()
    print "\nComputing bubblesort for N = %s" % N

    # Python
    start = time.time()
    x = bubblesort(randoms)
    print "Python \t%.5f sec" % (time.time() - start)
    assert np.all(sorted(randoms) == x)

    # Numba
    start = time.time()
    x = jitbubblesort(randoms)
    print "Numba \t%.5f sec" % (time.time() - start)
    assert np.all(sorted(randoms) == x)
