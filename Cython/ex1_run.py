
# To compile cython code!
import pyximport; pyximport.install()

from ex1_sort_cy import *
from ex1_sort_py import *
from ex1_sort_numba import *
from ex1_sort_parakeet import *

import random
import copy
import numpy as np

import timing

@timing.timed
def launch_function(func,l):
    return func(copy.copy(l)).all()

random.seed(4354353)
l = np.asarray([random.randint(1,1000) for num in xrange(1, 3000)])

l_sorted = np.sort(l)
for f in [python_bubblesort, python_bubblesort_cy, python_bubblesort_np,
          python_bubblesort_np_cy, cython_bubblesort,
          numba_bubblesort, parakeet_bubblesort]:
    print f,
    assert(l_sorted.all() == launch_function(f,l))
    print "\ttime: %.4f" % launch_function.timed()

print('Done!')
