# PythonParallel
Tests for Parallel Computing and Optimisation with Python

- Parallel Processing
 - Dask:
   - Great talk from SciPy: https://speakerdeck.com/jcrist/pandas-through-task-scheduling
 - DistArray
   - Notebook: https://github.com/enthought/distarray/blob/master/examples/features.ipynb
 - Xray
   - Extension to pandas for multi-dimensional and parallel processing
    - Notebook [here](http://nbviewer.ipython.org/urls/gist.githubusercontent.com/shoyer/be3749849809fe35efa8/raw/d3ac4af07343391ef005d2dbea80368efc9ee1f6/xray-demo-python-workers-party.ipynb).
 - IPython parallel
   - See other repo.
 - Pathos
   - MPI-based launcher, a ssh-based launcher, a multiprocessing launcher, a map-reduce algorithm. Pathos is divided into four subpackages:
      - dill: a utility for serialization of python objects
      - pox: utilities for filesystem exploration and automated builds
      - pyina: a MPI-based parallel mapper and launcher
      - pathos: distributed parallel map-reduce and ssh communication
- Optimisation
 - Cython
   - See examples in Python Tests repo.
 - Numba
   - Using just-in-time compilation.
