import os
import numpy as np
from sudoku import col_index_getter
from sudoku import get_cell_n_from_row_i

GRID_DIR = 'grids'

def load(filepath):
    return np.loadtxt(filepath, delimiter=",")

gridpath = os.path.join(GRID_DIR, 'sudoku.csv')
grid = load(gridpath)

# def test_grid(grid, a, b):
#     print (a==b, a, b)
#
# def get_from_saved_grid(n, cell):
#     i = (cell * 9) + n
#     return grid[i].nonzero()[0]
#
# def get_in_theory(n, squ, col, row):
#     c = (col * 9) + n
#     r = (row * 9) + n
#     s = (squ * 9) + n
#     return [c, r+81, s+81+81]
#
# def compare(n, squ, col, row, cell):
#     """ is the grid built correctly?
#         test col_index_getter against another function
#         and against the real returned grid
#     """
#
#     a = get_from_saved_grid(n, cell)
#     #b = get_in_theory(n, squ, col, row)
#     b = col_index_getter(3, col, row, n)
#     return a, b
#
#
# # n squ, col, row, cell
# tests = [   compare(3, 2, 6, 0, 6),
#             compare(7, 4, 4, 4, 40),
#             compare(8, 8, 8, 8, 80)
#         ]
#
# for test in tests:
#     pass
    #test_grid(grid, *test)

# def test_get_cell_n(N, row_i):
#     cell = row_i // (N**2)
#     n = row_i % (N**2)
#     return cell, n+1

#(701, 320), (685, 319), (669, 317), (655, 315), (645, 314), (633, 313)

print (get_cell_n_from_row_i(701))
