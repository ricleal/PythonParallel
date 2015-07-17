# PythonParallel
Tests for Parallel Computing and Optimisation with Python

# Parallel Processing

## Dask:

- Parallel computing (no need for launching a cluster)
- Talk from SciPy: https://speakerdeck.com/jcrist/pandas-through-task-scheduling

- dask.array = numpy + threading
- dask.bag = map, filter, toolz + multiprocessing
- dask.dataframe = pandas + threading

## DistArray

The Distributed Array Protocol (DAP) is a process-local protocol that allows two subscribers, called the producer and the consumer or the exporter and the importer, to communicate the essential data and metadata necessary to share a distributed-memory array between them.

- Needs IPython da cluster running: ```dacluster start -n4```
- Notebook: https://github.com/enthought/distarray/blob/master/examples/features.ipynb

## Xray

- Extension to pandas for multi-dimensional and parallel processing
- Notebook [here](http://nbviewer.ipython.org/urls/gist.githubusercontent.com/shoyer/be3749849809fe35efa8/raw/d3ac4af07343391ef005d2dbea80368efc9ee1f6/xray-demo-python-workers-party.ipynb).

## IPython parallel

- Needs IPython cluster running: ```ipcluster start -n 4```
- Or MPI cluster: ```ipcluster start --profile=mpi -n 4```

## Pathos
- MPI-based launcher, a ssh-based launcher, a multiprocessing launcher, a map-reduce algorithm. Pathos is divided into four subpackages:
  - dill: a utility for serialization of python objects
  - pox: utilities for filesystem exploration and automated builds
  - pyina: a MPI-based parallel mapper and launcher
  - pathos: distributed parallel map-reduce and ssh communication

# Optimisation

## Cython

- See examples in Python Tests repo.

## Numba

- Using just-in-time compilation.
