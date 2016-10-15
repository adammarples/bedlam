import algx
import numpy as np
from linked_lists import link_a_grid
import cProfile

def load(filepath):
    return np.loadtxt(filepath, delimiter=",")

def solve(name):
    grid = load('{}.csv'.format(name))
    print ('Load', name, '>', grid.shape)
    root = link_a_grid(grid)
    algx.run_solver(name, root)

def main():
    """https://www.ocf.berkeley.edu/~jchu/publicportal/sudoku/0011047.pdf
    """
    pass
    #solve('wiki_example')
    solve('soma')
    #solve('example')
    #solve('bedlam')
    #solve('knuth')

if __name__ == '__main__':
    pass
    #main()
    cProfile.run("main()")
