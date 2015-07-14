#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from pprint import pprint
from IPython.parallel import Client
'''

Launch in the shell an IPython the MPI cluster:

ipcluster start --profile=mpi -n 4

'''

c = Client(profile='mpi')
c.block = True # Computations run synchronously.

# All clusters!
view = c[:]

# Run / load the script:
view.run('psum.py')

# Set a in all clusters
view.scatter('a',np.arange(16,dtype='float'))
pprint(view['a'])

# excute and get the result
view.execute('b = psum(a)')
b = view['b']
pprint(b)
