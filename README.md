TODO expand to use `cudf`, `dask`ifiable regions, etc
ARRPKG ~ numpy
DFPFK ~ pandas

# Python+ Tests for replacing numpy operations

Limited implementation for replacing `numpy` array operations with a Python+ package
that has identical module/method names and call signatures (i.e. `cupy`). Dataframe
operations added soon, see TODO.

Execution scripts are in the top level for running tests of compute operations.
When creating a new test, the first thing to do is to set the array package 
as desired. See the file `pcca_test.py` which processes some input options, 
sets the array package, and runs some operation where the source code has
been modified to use the runtime-selected package.

## Current:
    PCCA from the msmtools package: https://github.com/markovmodel/msmtools

### Usage:

First, get some code with operations you want to replace. Copy into `src` 
folder (make new module if appropriate) and make these modifications:

```python
# At top after your imports
global ARRPKG
global DFPKG
ARRPKG = None
DFPKG = None

# Throughout the code
#np.linalg.norm(X)
#np.dot(X)
ARRPKG.linalg.norm(X)
ARRPKG.dot(X)
```

Then in your `test` file for this code, add this operation to let the
array package be set by an option at runtime:

```python
from src import my_new_code
from src.koopy_tools import set_array_package
#from src.koopy_tools import set_df_package

array_package = "cupy" # or numpy
#df_package = "cudf" # or pandas
set_array_package(my_new_code, array_package)
#set_df_package(my_new_code, df_package)
```

To use small default test case
    `python pcca_test.py`

--or--

To set up the execution configuration
    `python pcca_test.py [array_package] [input_file] [n_macrostates]`


