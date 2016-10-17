import numpy as np
import os
from build_matrix import save

SUDOKU_TEXT_DIR = 'sudoku_text'
GRID_DIR = 'grids'
N = 3

def load_sudoku(name):
    """ return an array from a text file.
    """
    filepath = os.path.join(SUDOKU_TEXT_DIR, '{}.txt'.format(name))
    with open(filepath, 'r') as fi:
        lines = fi.read().strip()
        text = [x for x in lines]
        while '\n' in text:
            text.remove('\n')
        array = np.array(text).reshape((9,9))
        return array

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
            row = grid[i]
            col_j = cell % 9
            row_i = cell // 9
            x = col_j // 3
            y = row_i // 3
            squ_k = (y * 3) + x
            col_mark = ((n * 9) + col_j)
            row_mark = ((n * 9) + col_j) + 81 - 1
            squ_mark = ((n * 9) + squ_k) + (2 * 81) - 1
            row[col_mark] = 1
            row[row_mark] = 1
            row[squ_mark] = 1
            i += 1
    print ('check', grid.sum()/3/81/9)
    return grid


if __name__ == '__main__':
    #main()
    #array = load_sudoku('example')
    #print (array)
    #grid = build_main_sudoku_grid()
    #filepath = os.path.join(GRID_DIR, 'sudoku.csv')
    #save(filepath, grid)
