import os
import cProfile
import numpy as np

from bedlam import GRID_DIR
from bedlam.linked_lists import link_a_grid
from bedlam.algx import run_solver
from bedlam.solution_builder import save


def load(filepath):
    return np.loadtxt(filepath, delimiter=",")

def solve(name):
    gridpath = os.path.join(GRID_DIR,'{}.csv'.format(name))
    grid = load(gridpath)
    print ('Load', name, '>', grid.shape)
    root = link_a_grid(grid)
    run_solver(name, root)

def main():
    """https://www.ocf.berkeley.edu/~jchu/publicportal/sudoku/0011047.pdf
    """
    pass
    #solve('wiki_example')
    #solve('example')
    #solve('knuth')
    #solve('hoffmann')
    #solve('coffin')
    #solve('nob')
    #solve('soma')
    #solve('bedlam')
    #solve('sudoku')

if __name__ == '__main__':
    pass
    main()
    #cProfile.run("main()")
