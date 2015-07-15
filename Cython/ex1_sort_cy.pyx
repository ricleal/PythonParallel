
import numpy as np
cimport numpy as np
cimport cython

@cython.boundscheck(False)
@cython.wraparound(False)
cpdef cython_bubblesort(inp_ary):
    """
    The Cython implementation of Bubblesort with NumPy memoryview.
    """
    cdef unsigned long length, i, swapped, ele, temp
    cdef long[:] np_ary = inp_ary
    length = np_ary.shape[0]
    swapped = 1
    for i in xrange(0, length):
        if swapped:
            swapped = 0
            for ele in xrange(0, length-i-1):
                if np_ary[ele] > np_ary[ele + 1]:
                    temp = np_ary[ele + 1]
                    np_ary[ele + 1] = np_ary[ele]
                    np_ary[ele] = temp
                    swapped = 1
    return inp_ary


### Same functions in .py but in a pyx


def python_bubblesort_cy(a_list):
    """
    Bubblesort in Python for list objects.
    """
    length = len(a_list)
    swapped = 1
    for i in xrange(0, length):
        if swapped:
            swapped = 0
            for ele in xrange(0, length-i-1):
                if a_list[ele] > a_list[ele + 1]:
                    temp = a_list[ele + 1]
                    a_list[ele + 1] = a_list[ele]
                    a_list[ele] = temp
                    swapped = 1
    return a_list

def python_bubblesort_np_cy(np_array):
    """
    Bubblesort in Python for NumPy arrays.
    """
    length = np_array.shape[0]
    swapped = 1
    for i in xrange(0, length):
        if swapped:
            swapped = 0
            for ele in xrange(0, length-i-1):
                if np_array[ele] > np_array[ele + 1]:
                    temp = np_array[ele + 1]
                    np_array[ele + 1] = np_array[ele]
                    np_array[ele] = temp
                    swapped = 1
    return np_array
