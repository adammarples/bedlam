import os
import numpy as np

GRID_DIR = 'grids'

def load(filepath):
    return np.loadtxt(filepath, delimiter=",")

gridpath = os.path.join(GRID_DIR, 'sudoku.csv')
grid = load(gridpath)

def test_grid(grid, a, b):
    print (a==b, a, b)

def get_a(n, cell):
    i = (cell * 9) + n
    return grid[i].nonzero()[0]

def get_b(n, squ, col, row):
    c = (col * 9) + n
    r = (row * 9) + n
    s = (squ * 9) + n
    return [c, r+81, s+81+81]

def get_ab(n, squ, col, row, cell):
    return get_a(n, cell), get_b(n, squ, col, row)

# n squ, col, row, cell
tests = [   get_ab(3, 2, 6, 0, 6),
            get_ab(7, 4, 4, 4, 40),
            get_ab(8, 8, 8, 8, 80)
        ]

for test in tests:
    test_grid(grid, *test)
