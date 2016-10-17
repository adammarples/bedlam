import numpy as np
import os
from build_matrix import save
from linked_lists import link_a_grid
from algx import search, run_solver, cover_column

SUDOKU_TEXT_DIR = 'sudoku_text'
GRID_DIR = 'grids'
N = 3

def load(filepath):
    return np.loadtxt(filepath, delimiter=",")

def load_sudoku(name):
    """ return an array from a text file.
    """
    filepath = os.path.join(SUDOKU_TEXT_DIR, '{}.txt'.format(name))
    with open(filepath, 'r') as fi:
        lines = fi.read().strip()
        text = [x for x in lines]
        while '\n' in text:
            text.remove('\n')
        text = [int(t) for t in text]
        array = np.array(text).reshape((9,9))
        return array

def col_index_getter(col_j, row_i, n):
    """ generate col indices that need to be filled with 1's.
    """
    x = col_j // 3
    y = row_i // 3
    squ_k = (y * 3) + x
    col_mark = ((n * 9) + col_j)
    row_mark = ((n * 9) + col_j) + 81 - 1
    squ_mark = ((n * 9) + squ_k) + (2 * 81) - 1
    return col_mark, row_mark, squ_mark

def row_index_getter(col_j, row_i, n):
    cell = (row_i * 9) + col_j
    return (cell * 9) + n 

def build_main_sudoku_grid():
    """
    columns are: (n**4) + (n**4) + (n**4)
        1incol1, 2incol1, ..., 9incol9,
        1inrow1, 2inrow1, ..., 9inrow9,
        1insqu1, 2insqu1, ..., 9insqu9.
    rows are: (n**2) * (m**2) * (n**2)
        1incel1, 2incel1, ..., 9incel9.

    """
    grid = np.zeros((9*81, 3*81))
    i = 0
    for cell in range(81):
        for n in range(9):
            col_j = cell % 9
            row_i = cell // 9
            i1, i2, i3 = col_index_getter(col_j, row_i, n)
            grid[i][i1] = 1
            grid[i][i2] = 1
            grid[i][i3] = 1
            i += 1
    print ('check', grid.sum()/3/81/9)
    return grid

def cover_column_by_indices(root, indices):
    solutions = []
    for index in indices[::-1]:
        c = root.r
        while c is not root:
            #print ('name', c.name, index)
            if c.name == index:

                c.remove_horiz()


                #solutions.append(c.d)
                break
            c = c.r
    return solutions

def solve_sudoku(name):
    gridpath = os.path.join(GRID_DIR, 'sudoku.csv')
    grid = load(gridpath)
    root = link_a_grid(grid)
    array = load_sudoku(name)
    #indices = []
    for (row_i, col_j), n in np.ndenumerate(array):
        if n:
            indices.extend(col_index_getter(col_j, row_i, n))
            #print (col_j, row_i, n)
    indices.sort()
    solutions = cover_column_by_indices(root, indices)
    uncovered = []
    c = root.r
    while c is not root:
        uncovered.append(c.name)
        c = c.r
    print (indices[::])
    print (uncovered)
    print ([node.name for node in solutions])
    #k = 0
    run_solver(name, root)
    #search(name, root, k, solutions)

def save_main_grid():
    grid = build_main_sudoku_grid()
    filepath = os.path.join(GRID_DIR, 'sudoku.csv')
    save(filepath, grid)

if __name__ == '__main__':
    save_main_grid()
    a = row_index_getter(0, 0, 0)
    b = row_index_getter(8, 8, 8)
    print (a, b)
    #solve_sudoku('example')
