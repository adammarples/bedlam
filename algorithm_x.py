import numpy as np 
from collections import defaultdict 
from string import ascii_uppercase

np.set_printoptions(linewidth=250)

def load(filepath):
    return np.loadtxt(filepath, delimiter=",")

def solver(grid, row_ids, partial_solution, level_dict, level):
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
    print('down at level', level, 'with bump', bump_row)
    if not grid.size:
        return partial_solution
    c = pick_column(grid)
    print('c =', c)
    r = pick_row(grid, c, bump_row)
    print('r =', r)
    if r is None:
        return
    print('putting', row_ids[r], 'in partial solution')
    partial_solution.append(row_ids[r])
    rows_to_keep, cols_to_keep = grid_magic(grid, c, r)
    new_grid = reduce_grid(grid, rows_to_keep, cols_to_keep)

    # Recursion
    level += 1
    #print 'rows to keep going in as', rows_to_keep, [row_ids[x] for x in rows_to_keep]partial = solver(new_grid, [row_ids[x] for x in rows_to_keep], partial_solution, level_dict, level)
    partial = solver(new_grid, [row_ids[x] for x in rows_to_keep], partial_solution, level_dict, level)
    if partial == None:
        print ('Failure!')
        # clear bumps on this level before leaving
        level_dict[level] = 0
        # step up the tree, add a bump
        level -= 1
        print ('go back a level to', level)
        level_dict[level] += 1
        print ('bump level', level, 'to row', level_dict[level])
        popped = partial_solution.pop()
        print (popped, 'removed from partial solution')
        #print 'partial solution now', partial_solution
        #print 'row_ids going in as', row_ids
        #run on old grid
        return solver(grid, row_ids, partial_solution, level_dict, level)
    else:
        return partial

def pick_column(grid):
    newmin = 1e6
    pick_idx = None
    for i, col in enumerate(grid.T):
        colsum = np.sum(col)
        if colsum < newmin:
            pick_idx = i
            newmin = colsum
        #print 'col', i, col
    #print 'pick col', pick_idx, 'as', pick_col
    return pick_idx

def pick_row(grid, col_ind, bump_row):
    #print 'picking row'
    #print grid.shape, col_ind
    for i, row in enumerate(grid):
        if row[col_ind]:
            if bump_row:
                bump_row -= 1
                #print 'bumping row', bump_row
                continue
            #print 'pick row', i, 'as', row
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
    #print 'rows to delete', rows_to_delete
    #print 'cols to delete', cols_to_delete
    #print 'rows to delete', set(rows_to_delete)
    #print 'cols to delete', set(cols_to_delete)
    cols_to_delete = set(cols_to_delete)
    rows_to_delete = set(rows_to_delete)
    cols_to_keep = [jj for jj in range(n) if jj not in cols_to_delete]
    rows_to_keep = [ii for ii in range(m) if ii not in rows_to_delete]
    #print 'rows to keep', rows_to_keep
    #print 'cols to keep', cols_to_keep
    return rows_to_keep, cols_to_keep

def reduce_grid(grid, rows_to_keep, cols_to_keep):

    #print 'grid to clean rows as'
    #print grid, grid.shape
    #print 'rows to keep as'
    #print '{}, len({})'.format(rows_to_keep, len(rows_to_keep))

    new_grid = np.take(grid, rows_to_keep, axis=0)
    #print 'cleaned grid as'
    #print new_grid, new_grid.shape

    #print 'cols to keep as'
    #print '{}, len({})'.format(cols_to_keep, len(cols_to_keep))

    new_grid = np.take(new_grid, cols_to_keep, axis=1)
    #print 'cleaned grid as'
    #print new_grid, new_grid.shape
    #print new_grid, new_grid.shape
    return new_grid

def solve_once(grid):
    m, n = grid.shape
    row_ids = range(m)
    partial_solution = []
    level_dict = defaultdict(int)
    level = 0
    solution = solver(grid, row_ids, partial_solution, level_dict, level)
    print ('solution as')
    print (solution)
    solution_grid = np.take(grid, solution, axis=0)
    print (solution_grid)
    #print (solution_grid.shape, (n_shapes, box_size**3+n_shapes))
    #print (solution_grid.shape == (n_shapes, box_size**3+n_shapes))
    print (np.sum(solution_grid, axis=0).all())
    return solution, level_dict
    

if __name__ == '__main__':
    pass