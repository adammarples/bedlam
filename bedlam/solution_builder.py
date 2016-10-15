import os
import numpy as np

SAVED_SOLUTION_DIR = 'saved_solutions'

def generate_arrays(name):
    filename = os.path.join(SAVED_SOLUTION_DIR, '{}_solutions.txt'.format(name))
    with open(filename, 'r') as fi:
        for line in fi.readlines():
            array = np.array([int(x) for x in (line.strip())[1:-1].split(', ')])
            yield array

def main():
    for array in generate_arrays('soma'):
        print (array)

if __name__ == '__main__':
    main()
