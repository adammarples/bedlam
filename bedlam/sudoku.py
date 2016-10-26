import numpy as np
import os
from build_matrix import save
from linked_lists import link_a_grid
from algx import run_solver, cover_column, search
from solution_builder import generate_arrays

np.set_printoptions(linewidth=250)
GRID_DIR = 'grids'
SAVED_SOLUTION_DIR = 'saved_solutions'
SUDOKUS_DIR = 'sudoku_boxes'
SUDOKU_TEXT_DIR = 'sudoku_text'

def load(filepath):
    return np.loadtxt(filepath, delimiter=",")

def load_sudoku(name, N):
    """ return an array from a text file.
    """
    filepath = os.path.join(SUDOKU_TEXT_DIR, '{}.txt'.format(name))
    with open(filepath, 'r') as fi:
        lines = fi.read().strip()
        text = [x for x in lines]
        while '\n' in text:
            text.remove('\n')
        text = [int(t) for t in text]
        array = np.array(text).reshape((N**2,N**2))
        return array

def col_index_getter(N, col_j, row_i, n):
    """ generate col indices that need to be filled with 1's.
    """
    x = col_j // N
    y = row_i // N
    squ_k = (y * N) + x
    col_mark = ((col_j * (N**2)) + n)
    row_mark = ((row_i * (N**2)) + n) + (1 * (N**4))
    squ_mark = ((squ_k * (N**2)) + n) + (2 * (N**4))
    cel_mark = ((row_i * (N**2)) + col_j) + (3 * (N**4))
    return col_mark, row_mark, squ_mark, cel_mark

def row_index_getter(N, col_j, row_i, n):
    cell = (row_i * (N**2)) + col_j
    return (cell * (N**2)) + n

def build_main_sudoku_grid(N):
    """
    columns are: (n**4) + (n**4) + (n**4)
        1incol1, 2incol1, ..., 9incol9,
        1inrow1, 2inrow1, ..., 9inrow9,
        1insqu1, 2insqu1, ..., 9insqu9.
        cell1filled, ..., cell81filled
    rows are: (n**2) * (m**2) * (n**2)
        1incel1, 2incel1, ..., 9incel9.

    """
    grid = np.zeros((N**6, 4*(N**4)))
    i = 0
    # these two loops make 81*9 rows
    for cell in range(N**4):
        for n in range(N**2):
            # col_j row_i are cols/rows in the sudoku board, 0-8 each
            col_j = cell % (N**2)
            row_i = cell // (N**2)
            i1, i2, i3, i4 = col_index_getter(N, col_j, row_i, n)
            #print ('cell', cell, 'n', n, 'col', col_j, 'row', row_i, 'indices', i1, i2, i3)
            grid[i][i1] = 1
            grid[i][i2] = 1
            grid[i][i3] = 1
            grid[i][i4] = 1
            i += 1
    print ('check', grid.sum()/4/N**6)
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
                    #
                    rnod = node.r
                    while rnod is not node:
                        cover_column(rnod.c)
                        rnod = rnod.r
                    #
                node = node.d
            c = c.r
    return solutions

def solve_sudoku(name, N):
    gridpath = os.path.join(GRID_DIR, 'sudoku_{}.csv'.format(N))
    grid = load(gridpath)
    root = link_a_grid(grid)
    solutions = []
    array = load_sudoku(name, N)
    nodes = []
    for (row_i, col_j), n in np.ndenumerate(array):
        if n:
            row_index = row_index_getter(N, col_j, row_i, n)
            col_indices = col_index_getter(N, col_j, row_i, n)
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
    answer = search(name, root, k, solutions)
    print (answer)

def save_sudoku_grid(N):
    grid = build_main_sudoku_grid(N)
    filepath = os.path.join(GRID_DIR, 'sudoku_{}.csv'.format(N))
    save(filepath, grid)

# def reverse_getter(i1, i2, i3):
#     col_j = i1 // 9
#     n = i1 % 9
#     row_i = (i2 - 81) // 9
#     print (col_j, row_i, n+1)
#     cell = (row_i * 9) + col_j
#     return cell, n+1

def get_cell_n_from_row_i(N, row_i):
    cell = row_i // (N**2)
    n = row_i % (N**2)
    return cell, n+1

def build_sudoku_solutions(name, N):
    gridpath = os.path.join(GRID_DIR, 'sudoku_{}.csv'.format(N))
    grid = load(gridpath)
    for array in generate_arrays(name):
        #print (array, array.shape)
        solution = np.take(grid, array, axis=0)
        #print (solution)
        #print (solution.shape)
        sumline = solution.sum(axis=0)
        status = 'full', sumline.all(), 'even', sumline.sum()==len(sumline)
        print (status, sumline.shape)
        answers = []
        for row_i in array:
            cell, n = get_cell_n_from_row_i(N, row_i)
            answers.append((cell, n))
        #print (answers)
        answers.sort()
        #print (answers)
        flat = np.array([a for a in zip(*answers)][1])
        field = flat.reshape((N**2, N**2))
        print ('field')
        print (field)
        yield field

if __name__ == '__main__':
    #save_sudoku_grid(2)
    #save_sudoku_grid(3)
    #solve_sudoku('blank2', 2)
    #solve_sudoku('blank', 3)
    #solve_sudoku('sudoku_example', 3)
    [x for x in build_sudoku_solutions('blank2', 2)]
    #[x for x in build_sudoku_solutions('blank', 3)]
    #[x for x in build_sudoku_solutions('sudoku_example', 3)]
