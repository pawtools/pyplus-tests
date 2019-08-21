TODO expand to use `cudf`, `dask`ifiable regions, etc
ARRPKG ~ numpy
DFPFK ~ pandas

# Python+ Tests for replacing numpy operations

Limited implementation for replacing `numpy` operations with a Python+ package
that has identical module/method names and call signatures (i.e. `cupy`).

Execution scripts are in the top level for running tests of compute operations.
When creating a new test, the first thing to do is to set the compute package 
as desired. See the file `pcca_test.py` which processes some input options, 
sets the compute package, and runs some operation where the source code has
been modified to use the runtime-selected package.

## Current:
    PCCA from the msmtools package: https://github.com/markovmodel/msmtools

### Usage:

First, get some code with operations you want to replace. Copy into `src` 
folder (make new module if appropriate) and make these modifications:

```python
# At top after your imports
global ARRPKG
ARRPKG = None

# Throughout the code
#np.linalg.norm(X)
#np.dot(X)
ARRPKG.linalg.norm(X)
ARRPKG.dot(X)
```

Then in your `test` file for this code, add this operation to let the
compute package be set by an option at runtime:

```python
from src import my_new_package
from src.koopy_tools import set_compute_package

compute_package = "cupy" # or numpy
set_compute_package(my_new_package, compute_package)
```

To use small default test case
    `python pcca_test.py`

--or--

To set up the execution configuration
    `python pcca_test.py [compute_package] [input_file] [n_macrostates]`


