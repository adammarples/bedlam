import algx
import numpy as np
from linked_lists import link_a_grid

def load(filepath):
    return np.loadtxt(filepath, delimiter=",")

def solve(name):
    grid = load('{}.csv'.format(name))
    print ('Load', name, '>', grid.shape)
    root = link_a_grid(grid)
    algx.run_solver(root)

if __name__ == '__main__':
    """https://www.ocf.berkeley.edu/~jchu/publicportal/sudoku/0011047.pdf
    """
    #solve('wiki_example')
    #solve('soma')
    #solve('example')
    #solve('bedlam')
    solve('knuth')
