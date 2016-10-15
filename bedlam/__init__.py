GRID_DIR = 'grids'
TEXT_DIR = 'text'
SOLUTION_DIR = 'solutions'

import numpy as np

def load(filepath):
    return np.loadtxt(filepath, delimiter=",")

# import bedlam.algx
# import bedlam.linked_lists
# import bedlam.builder
# import bedlam.build_matrix
# import bedlam.coordinate_handler
# import bedlam.shape_reader
