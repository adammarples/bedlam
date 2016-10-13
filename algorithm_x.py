import numpy as np
from collections import defaultdict
from string import ascii_uppercase

np.set_printoptions(linewidth=250)

def load(filepath):
    return np.loadtxt(filepath, delimiter=",")

def saving(solution, name):
    with open('{}_solutions.txt'.format(name), 'a') as fi:
        print (solution, file=fi)
        # for item in solution:
        #     fi.write(str(item))
        #     fi.write(', ')
        # fi.write('/n')

def solver(name, grid, col_ids, row_ids, partial_solution, level_dict, level):
    """ incidence matrix solver from d. e. knuth's "algorith x"

    From Wikipedia:
    1. If the matrix A has no columns, the current partial solution
    is a valid solution; terminate successfully.
    2. Otherwise choose a column c (deterministically). (We are choosing the column
    with the least number of 0's (why?)).
    3. Choose a row r such that A[r][c] == 1 (nondeterministically). (We
    are simply iterating through the rows in order).
    4. Include row r in the partial solution.
    5. for each column j such that A[r][j] == 1:
          for each row i such that A[i][j] == 1:
               delete row i from matrix A.
          delete column j from matrix A.
    """

    bump_row = level_dict[level]
    if not grid.size:
        print( 'grid is empty, success.')
        saving(partial_solution, name)
        return
    c = pick_column(grid)
    r = pick_row(grid, c, bump_row)
    if r is None:
        print ('r is None, impossible grid.')
        return
    print('putting', row_ids[r], 'in partial solution')
    partial_solution.append(row_ids[r])
    rows_to_delete, cols_to_delete, rows_to_keep, cols_to_keep = grid_magic(grid, c, r)
    new_grid = reduce_grid(grid, rows_to_delete, cols_to_delete, rows_to_keep, cols_to_keep,  row_ids, col_ids)
    # Recursion
    level += 1
    new_col_ids = [col_ids[x] for x in cols_to_keep]
    new_row_ids = [row_ids[x] for x in rows_to_keep]
    solver(name, new_grid, new_col_ids, new_row_ids, partial_solution, level_dict, level)
    # clear bumps on this level before leaving
    level_dict[level] = 0
    # step up the tree, add a bump
    level -= 1
    #print ('go back a level to', level)
    level_dict[level] += 1
    #print ('bump level', level, 'to row', level_dict[level])
    popped = partial_solution.pop()
    print (popped, 'removed from partial solution')
    solution = solver(name, grid, col_ids, row_ids, partial_solution, level_dict, level)
    print ('Recursion level finished.')
    print ('Solution', solution)
    return

def pick_column(grid):
    newmin = 1e6
    pick_idx = None
    for i, col in enumerate(grid.T):
        colsum = np.sum(col)
        if colsum < newmin:
            pick_idx = i
            newmin = colsum
    return pick_idx

def pick_row(grid, col_ind, bump_row):
    for i, row in enumerate(grid):
        if row[col_ind]:
            if bump_row:
                bump_row -= 1
                continue
            return i

def grid_magic(grid, c, r):
    cols_to_delete = []
    rows_to_delete = []
    m, n = grid.shape
    for j in range(n):
        if grid[r][j]:
            for i in range(m):
                if grid[i][j]:
                    rows_to_delete.append(i)
            cols_to_delete.append(j)
    cols_to_delete = set(cols_to_delete)
    rows_to_delete = set(rows_to_delete)
    rows_to_keep = [ii for ii in range(m) if ii not in rows_to_delete]
    cols_to_keep = [jj for jj in range(n) if jj not in cols_to_delete]
    return rows_to_delete, cols_to_delete, rows_to_keep, cols_to_keep

def reduce_grid(grid, rows_to_delete, cols_to_delete, rows_to_keep, cols_to_keep, row_ids, col_ids):
    #print ('deleting columns', [col_ids[j]+1 for j in cols_to_delete])
    new_grid = np.take(grid, cols_to_keep, axis=1)
    #print ('deleting rows', [ascii_uppercase[row_ids[i]] for i in rows_to_delete])
    new_grid = np.take(new_grid, rows_to_keep, axis=0)
    return new_grid

def run_solver(grid, name):
    m, n = grid.shape
    col_ids = range(n)
    row_ids = range(m)
    partial_solution = []
    level_dict = defaultdict(int)
    level = 0
    solver(name, grid, col_ids, row_ids, partial_solution, level_dict, level)


if __name__ == '__main__':
    name = 'wiki_example'
    grid = load('{}.csv'.format(name))
    print ('Load', name, '>', grid.shape)
    run_solver(grid, name)
