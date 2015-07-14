#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

from IPython import parallel

'''

Launch in the shell an IPython cluster:

# 4 processors
ipcluster start -n 4
# As many as possible
ipcluster start

'''
def distance(a,b):
    '''
    Function to executed in the cluster
    euclidean distance
    '''
    dist = np.linalg.norm(a-b)
    return dist

def get_clients():
    clients = parallel.Client()
    clients.block = True  # use synchronous computations
    print "Clients running:", clients.ids
    return clients

def set_views(clients):
    '''
    synchronise imports
    '''
    dview = clients.direct_view()
    dview.block = True # all results must finish computing before any results are recorded
    dview.execute('import numpy as np')

def test_cluster(clients,n):
    '''
    '''
    res = clients[n].apply(distance, np.array([1,2]), np.array([2,3]))
    return res

def test_load_balanced(clients,a_arr,b_arr):
    '''
    Sort of multithreading map. Every element in the arrays will be
    executed in parallel
    '''
    assert len(a_arr) == len(b_arr)
    view = clients.load_balanced_view() # allows execution of a command on any one engine. Which engine is used is up to the scheduler
    #view = clients.direct_view() # direct execution of a command on all the engines
    res = view.map(distance, a_arr,b_arr)
    return res

def test_run_remote(clients,script_path):
    view = clients.direct_view()
    view.run(script_path)

def main():
    clients = get_clients()
    set_views(clients)

    # test 1 cluster
    res = test_cluster(clients,n=0)
    print 'Test cluster 0:', res

    # test: 2 arrays of 3d points in space
    a = np.random.random_integers(1,10,(10, 3))
    b = np.random.random_integers(20,50,(10, 3))
    res = test_load_balanced(clients,a,b)
    print 'Test load balanced:', res



if __name__ == "__main__":
    main()
