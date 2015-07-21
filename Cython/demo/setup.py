#!/usr/bin/env python

"""
Run as:

python setup.py build_ext --inplace


Or, instead of using this file, the following should also work:
#
cython my_package.pyx

# Compile the object file
gcc -c -fPIC -I/usr/include/python2.7/ my_package.c

# Link it into a shared library
gcc -shared my_package.o -o my_package.so

"""

from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("my_package.pyx"),
)
