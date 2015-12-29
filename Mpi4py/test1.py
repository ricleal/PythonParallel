#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

import h5py
import sys


class FileHandler(object):

    def __init__(self, filename):
        self.h5f = h5py.File(filename, "r")

    def __call__(self):
        return self.h5f

    def __del__(self):
        self.h5f.close()

def test_file_text_field(f):
    print f['entry']['notes'].value
    print f['entry']['notes'].value[0]
    print f['entry']['notes'].shape
    print f['entry']['notes'].dtype

def test_data_field(f):
    data = f['entry']['bank11']['data']
    print data.shape
    print data.chunks


if __name__ == '__main__':
    default_filename = "/SNS/MANDI/IPTS-12697/0/4089/NeXus/MANDI_4089_histo.nxs"
    f = FileHandler(default_filename)
    test_file_text_field(f())
    test_data_field(f())
