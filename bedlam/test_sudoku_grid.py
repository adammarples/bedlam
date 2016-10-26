import os
import numpy as np
from sudoku import col_index_getter

GRID_DIR = 'grids'

def load(filepath):
    return np.loadtxt(filepath, delimiter=",")

gridpath = os.path.join(GRID_DIR, 'sudoku.csv')
grid = load(gridpath)

def test_grid(grid, a, b):
    print (a==b, a, b)

def get_from_saved_grid(n, cell):
    i = (cell * 9) + n
    return grid[i].nonzero()[0]

def get_in_theory(n, squ, col, row):
    c = (col * 9) + n
    r = (row * 9) + n
    s = (squ * 9) + n
    return [c, r+81, s+81+81]

def compare(n, squ, col, row, cell):
    a = get_from_saved_grid(n, cell)
    b = get_in_theory(n, squ, col, row)
    b = col_index_getter(col, row, n)
    return a, b

#col_index_getter(col_j, row_i, n)

# n squ, col, row, cell
tests = [   compare(3, 2, 6, 0, 6),
            compare(7, 4, 4, 4, 40),
            compare(8, 8, 8, 8, 80)
        ]

for test in tests:
    test_grid(grid, *test)

# is the grid built correctly?
# test col_index_getter against another function
