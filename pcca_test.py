
import os
import sys

import src


# If no args given, defaults:
compute_package         = "numpy"
input_transition_matrix = "P89.npy"
n_macrostates           = 10

if __name__ == "__main__":

    if len(sys.argv) == 4:

        compute_package         = sys.argv[1]
        input_transition_matrix = sys.argv[2]
        n_macrostates           = sys.argv[3]

        assert os.path.exists(input_transition_matrix)
        assert n_macrostates.find('.') < 0

    src.koopy_tools.set_compute_package(src.pcca, compute_package)

    T = pcca_standalone_koopy.CPT.load(input_transition_matrix)
    N = int(n_macrostates)

    src.PCCA(T, N)
