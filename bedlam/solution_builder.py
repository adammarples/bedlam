import os
import numpy as np
from __init__ import load

np.set_printoptions(linewidth=150)

GRID_DIR = 'grids'
SAVED_SOLUTION_DIR = 'saved_solutions'
BOXES_DIR = 'boxes'
try:
    os.stat(BOXES_DIR)
except:
    print ('Creating', BOXES_DIR)
    os.mkdir(BOXES_DIR)

def generate_arrays(name):
    filename = os.path.join(SAVED_SOLUTION_DIR, '{}_solutions.txt'.format(name))
    with open(filename, 'r') as fi:
        for line in fi.readlines():
            array = np.array([int(x) for x in (line.strip())[1:-1].split(', ')])
            yield array

def build(name, n_shapes, box_size):
    gridpath = os.path.join(GRID_DIR,'{}.csv'.format(name))
    grid = load(gridpath)
    for array in generate_arrays(name):
        print (array)
        solution = np.take(grid, array, axis=0)
        sumline = solution.sum(axis=0)
        status = 'full', sumline.all(), 'even', sumline.sum()==len(sumline)
        print (status)
        for line in solution:
            shape_code = (np.where(line[-n_shapes:])[0][0]) + 1
            line[line==True] = shape_code
        flat_solution = (solution.sum(axis=0))[:-n_shapes]
        box = flat_solution.reshape((box_size, box_size, box_size))
        yield array, box, status

def save(name, n_shapes, box_size):
    filepath = os.path.join(BOXES_DIR, '{}_box.txt'.format(name))
    with open(filepath, 'w') as fi:
        for array, box, status in build(name, n_shapes, box_size):
            print (array, file=fi)
            print (status, file=fi)
            print (box, file=fi)
            print ('#', file=fi)

def main():
    save('soma', 7, 3)
    #save('bedlam', 13, 4)

if __name__ == '__main__':
    main()
