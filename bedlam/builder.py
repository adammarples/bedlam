import build_matrix as bx
import os

GRID_DIR = 'grids'
try:
    os.stat(GRID_DIR)
except:
    print ('Creating', GRID_DIR)
    os.mkdir(GRID_DIR)
TEXT_DIR = 'text'

def build_soma():

    grid = bx.build_from_txt(os.path.join(TEXT_DIR, 'soma.txt'), 7, 3)
    bx.save(os.path.join(GRID_DIR, 'soma.csv'), grid)

def build_bedlam():
    grid = bx.build_from_txt(os.path.join(TEXT_DIR, 'bedlam.txt'), 13, 4)
    bx.save(os.path.join(GRID_DIR, 'bedlam.csv'), grid)

def build_wiki_example():
    universe = {1, 2, 3, 4, 5, 6, 7}
    A = {1, 4, 7}
    B = {1, 4}
    C = {4, 5, 7}
    D = {3, 5, 6}
    E = {2, 3, 6, 7}
    F = {2, 7}
    sets = [A, B, C, D, E, F]
    grid = bx.build_from_sets(universe, sets)
    bx.save(os.path.join(GRID_DIR, 'wiki_example.csv'), grid)

def build_example():
    S = {1, 2, 3, 4, 5}
    A1 = {1, 5}
    A2 = {2, 4}
    A3 = {2, 3}
    A4 = {3}
    A5 = {1, 4, 5}
    sets = [A1, A2, A3, A4, A5]
    grid = bx.build_from_sets(S, sets)
    bx.save(os.path.join(GRID_DIR, 'example.csv'), grid)

def build_knuth():
    S = {1, 2, 3, 4, 5, 6, 7}
    A1 = {3, 5, 6}
    A2 = {1, 4, 7}
    A3 = {2, 3, 6}
    A4 = {1, 4}
    A5 = {2, 7}
    A6 = {4, 5, 7}
    sets = [A1, A2, A3, A4, A5, A6]
    grid = bx.build_from_sets(S, sets)
    bx.save(os.path.join(GRID_DIR, 'knuth.csv'), grid)

if __name__ == '__main__':
    pass
    build_wiki_example()
    build_soma()
    build_example()
    build_bedlam()
    build_knuth()
