import numpy as np
import os

from .build_matrix import save
from .linked_lists import link_a_grid
from .algx import run_solver, cover_column, search
from .solution_builder import generate_arrays

from bedlam import GRID_DIR, SOLUTION_DIR, SUDOKUS_DIR, SUDOKU_TEXT_DIR

np.set_printoptions(linewidth=250)
N = 3

def load(filepath):
    return np.loadtxt(filepath, delimiter=",")

def load_sudoku(name):
    """ return an array from a text file.
    """
    filepath = os.path.join(SUDOKU_TEXT_DIR, '{}.txt'.format(name))
    with open(filepath, 'r') as fi:
        print (fi.read())
        fi.seek(0)
        arr = []
        lines = fi.readlines()
        for line in lines:
            split = line.strip().split(' ')

            ints = [0 if x=='.' else int(x) for x in split]
            arr.append(ints)
        array = np.array(arr).reshape((N**2,N**2))
        return array

def col_index_getter(col_j, row_i, n):
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

def row_index_getter(col_j, row_i, n):
    cell = (row_i * (N**2)) + col_j
    return (cell * (N**2)) + n

def build_main_sudoku_grid():
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
            i1, i2, i3, i4 = col_index_getter(col_j, row_i, n)
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
                    solutions.append(node)
                    cover_column(node.c)

                    rnod = node.r
                    while rnod is not node:
                        cover_column(rnod.c)
                        rnod = rnod.r

                node = node.d
            c = c.r
    #print ('Fixed solutions', [no.name for no in solutions])
    return solutions

def solve_sudoku(name):
    savepath = os.path.join(SOLUTION_DIR, '{}_solutions.txt'.format(name))
    if os.path.isfile(savepath):
        print ('Deleting', savepath)
        os.remove(savepath)

    gridpath = os.path.join(GRID_DIR, 'sudoku.csv')
    grid = load(gridpath)
    root = link_a_grid(grid)
    solutions = []
    array = load_sudoku(name)
    nodes = []
    #print (array)
    for (row_i, col_j), n in np.ndenumerate(array):
        if n:
            row_index = row_index_getter(col_j, row_i, n-1)
            col_indices = col_index_getter(col_j, row_i, n-1)
            node_name = (col_indices[-1], row_index)
            nodes.append(node_name)
    nodes.sort()
    nodes.reverse()
    #print ('Removing fixed numbers')
    solutions = cover_column_by_nodes(root, nodes)
    uncovered = []
    c = root.r
    while c is not root:
        uncovered.append(c.name)
        c = c.r
    k = 0
    search(name, root, k, solutions)

def save_sudoku_grid():
    grid = build_main_sudoku_grid()
    filepath = os.path.join(GRID_DIR, 'sudoku.csv')
    save(filepath, grid)

def get_cell_n_from_row_i(row_i):
    cell = row_i // (N**2)
    n = row_i % (N**2)
    return cell, n+1

def build_sudoku_solutions(name):
    gridpath = os.path.join(GRID_DIR, 'sudoku.csv')
    grid = load(gridpath)
    solpath = os.path.join(SUDOKUS_DIR, '{}_box.txt'.format(name))
    with open(solpath, 'w') as fi:
        for array in generate_arrays(name):
            solution = np.take(grid, array, axis=0)
            sumline = solution.sum(axis=0)
            status = 'full', sumline.all(), 'even', sumline.sum()==len(sumline)
            print (status, sumline.shape)
            print (status, sumline.shape, file=fi)
            answers = []
            for row_i in array:
                cell, n = get_cell_n_from_row_i(row_i)
                answers.append((cell, n))
            answers.sort()
            flat = np.array([a for a in zip(*answers)][1])
            field = flat.reshape((N**2, N**2))
            for line in field:
                print (''.join([str(x) + ' ' for x in line]))
                print (''.join([str(x) + ' ' for x in line]), file=fi)
            #print ('field')
            #print (field)
            #print (field, file=fi)
            yield field

def solve_and_build(name):
    solve_sudoku(name)
    build_sudoku(name)

def build_sudoku(name):
    [x for x in build_sudoku_solutions(name)]

if __name__ == '__main__':
    pass
    #save_sudoku_grid()
    #solve_sudoku('blank')
    #solve_sudoku('sudoku_example')
    #solve_sudoku('x')
    #[x for x in build_sudoku_solutions('blank')]
    #[x for x in build_sudoku_solutions('sudoku_example')]
    #solve_sudoku('blank')
    #build_sudoku('blank')
    #solve_and_build('blank')
    #solve_and_build('sudoku_example')
    #solve_and_build('x')
    #solve_and_build('japanese')
    solve_and_build('worstcase')
