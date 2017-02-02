GRID_DIR = 'grids'
TEXT_DIR = 'text'
SOLUTION_DIR = 'solutions'
BOXES_DIR = 'boxes'
SUDOKUS_DIR = 'sudoku_boxes'
SUDOKU_TEXT_DIR = 'sudoku_text'

import numpy as np
def load(filepath):
    return np.loadtxt(filepath, delimiter=",")

saved_dict = {  'hoffmann': (6, 3),
                'coffin': (6, 3),
                'nob': (6, 3),
                'soma': (7, 3),
                'bedlam': (13, 4),
            }
