
import os
import sys
import pcca_standalone_koopy


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

    pcca_standalone_koopy.set_compute_package(compute_package)

    T = pcca_standalone_koopy.CPT.load(input_transition_matrix)
    N = int(n_macrostates)

    pcca_standalone_koopy.PCCA(T, N)
