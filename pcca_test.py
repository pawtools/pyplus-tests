
import os
import sys

from src.koopy_tools import set_array_package
from src import pcca


# If no args given, defaults:
array_package           = "numpy"
input_transition_matrix = "inputs/P89.npy"
n_macrostates           = 10

if __name__ == "__main__":

    if len(sys.argv) == 4:

        array_package           = sys.argv[1]
        input_transition_matrix = sys.argv[2]
        n_macrostates           = sys.argv[3]

        assert os.path.exists(input_transition_matrix)
        assert n_macrostates.find('.') < 0

    set_array_package(pcca, array_package)

    T = pcca.ARRPKG.load(input_transition_matrix)
    N = int(n_macrostates)

    pcca.PCCA(T, N)
