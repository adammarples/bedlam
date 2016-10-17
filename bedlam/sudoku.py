import numpy as np
import os
from build_matrix import save
from linked_lists import link_a_grid
from algx import run_solver, cover_column, search

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

def cover_column_by_nodes(root, nodes):
    solutions = []
    for node_xy in nodes:
        (y, x) = node_xy
        node_xy = (x, y)
        c = root.r
        while c is not root:
            node = c.d
            while node is not c:
                if node.name == node_xy:
                    #print ('SOLUTION', node.c.name)
                    solutions.append(node)
                    cover_column(node.c)
                node = node.d
            c = c.r
    return solutions

def solve_sudoku(name):
    gridpath = os.path.join(GRID_DIR, 'sudoku.csv')
    grid = load(gridpath)
    root = link_a_grid(grid)
    array = load_sudoku(name)
    nodes = []
    for (row_i, col_j), n in np.ndenumerate(array):
        if n:
            row_index = row_index_getter(col_j, row_i, n)
            col_indices = col_index_getter(col_j, row_i, n)
            node_name = (col_indices[-1], row_index)
            nodes.append(node_name)
            #print (col_j, row_i, n)
    nodes.sort()
    nodes.reverse()
    print ('Removing fixed numbers')
    solutions = cover_column_by_nodes(root, nodes)
    uncovered = []
    c = root.r
    while c is not root:
        uncovered.append(c.name)
        c = c.r
    k = 0
    search(name, root, k, solutions)

def save_main_grid():
    grid = build_main_sudoku_grid()
    filepath = os.path.join(GRID_DIR, 'sudoku.csv')
    save(filepath, grid)

if __name__ == '__main__':
    save_main_grid()
    a = row_index_getter(0, 0, 0)
    b = row_index_getter(8, 8, 8)
    print (a, b)
    solve_sudoku('example')
