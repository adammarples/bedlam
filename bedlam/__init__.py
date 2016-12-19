GRID_DIR = 'grids'
TEXT_DIR = 'text'
SOLUTION_DIR = 'solutions'
BOXES_DIR = 'boxes'
SUDOKUS_DIR = 'sudoku_boxes'
SUDOKU_TEXT_DIR = 'sudoku_text'

import numpy as np

def load(filepath):
    return np.loadtxt(filepath, delimiter=",")
