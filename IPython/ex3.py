#!/usr/bin/env python
# -*- coding: utf-8 -*-

from IPython import parallel
import tempfile

'''

Launch in the shell an IPython cluster:

# 4 processors
ipcluster start -n 4

'''

c = parallel.Client(packer='pickle')
c.block = True
print(c.ids)

dview = c.direct_view()
dview.block = True
print(dview)

dview.execute('import numpy as np')

###using execute
dview.execute('a=np.random.randint(0,5,size=(1,2))')
print("a:\n{}".format(dview.gather('a')))

###using run
temp = tempfile.NamedTemporaryFile()
try:
    temp.write('import numpy as np\nb=np.zeros(shape=(1,4),dtype=np.int32)')
    temp.flush()
    dview.run(temp.name)
finally:
    temp.close() # deletes the file!
print("b:\n{}".format(dview.gather('b')))
print type(dview.gather('b')[0,0])

###using dictionary
dview['c']=np.ones(shape=(2,3),dtype=np.int8)
print("a:\n{}".format(dview.gather('c')))
print type(dview.gather('c')[0,0])
