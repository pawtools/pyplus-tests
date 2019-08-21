
# Python+ Tests for replacing numpy operations

Limited implementation for replacing `numpy` operations with a Python+ package
that has identical module/method names and call signatures (i.e. `cupy`).

TODO expand to use `cudf`, `dask`ifiable regions, etc

Execution scripts are in the top level for running tests of compute operations.
When creating a new test, the first thing to do is to set the compute package 
as desired. See the file `pcca_test.py` which processes some input options, 
sets the compute package, and runs some operation where the source code has
been modified to use the runtime-selected package.

## Current:
    PCCA from the msmtools package: https://github.com/markovmodel/msmtools


### Usage:

To use small default test case
    python pcca_test.py

--or--

To set up the execution configuration
    python pcca_test.py [compute_package] [input_file] [n_macrostates]


