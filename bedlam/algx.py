import os
import numpy as np
from bedlam import SOLUTION_DIR

try:
    os.stat(SOLUTION_DIR)
except:
    print ('Creating', SOLUTION_DIR)
    os.mkdir(SOLUTION_DIR)

def search(name, root, k, solutions):
    if root == root.r:
        solution_path = os.path.join(SOLUTION_DIR, '{}_solutions.txt'.format(name))
        with open(solution_path, 'a') as fi:
            print ([n.name[0] for n in solutions], file=fi)
        print ('Solution found', np.array([n.name[0] for n in solutions]))
        return
    c = pick_column(root)
    #print ('cover column', c.name)
    cover_column(c)
    node = c.d
    while node is not c:
        #print ('add to solution', node.name)
        solutions.append(node)
        rnod = node.r
        while rnod is not node:
            #print ('r cover column', rnod.name)
            cover_column(rnod.c)
            rnod = rnod.r
        search(name, root, k+1, solutions)
        node = solutions.pop()
        #print ('pop', node.name)
        c = node.c
        lnod = node.l
        while lnod is not node:
            #print ('l uncover column', lnod.name)
            uncover_column(lnod.c)
            lnod = lnod.l
        node = node.d
    #print ('uncover column', c.name)
    uncover_column(c)

def run_solver(name, root):
    k = 0
    solutions = []
    search(name, root, k, solutions)

def pick_column(root):
    # Pick a column deterministically
    s = 1e6
    c = root
    node = root.r
    while node is not root:
        if node.s < s:
            c = node
            s = node.s
        node = node.r
    return c

def cover_column(c):
    # "Cover" column c
    c.remove_horiz()
    node = c.d
    while node is not c:
        rnod = node.r
        while rnod is not node:
            rnod.remove_vert()
            rnod.c.s -= 1
            rnod = rnod.r
        node = node.d

def uncover_column(c):
    # "Uncover" column c
    node = c.u
    while node is not c:
        lnod = node.l
        while lnod is not node:
            lnod.insert_vert()
            lnod.c.s += 1
            lnod = lnod.l
        node = node.u
    c.insert_horiz()

def main():
    from main import load, link_a_grid
    name = 'soma'
    grid = load('{}.csv'.format(name))
    print ('Load', name, '>', grid.shape)
    root = link_a_grid(grid)
    run_solver(name, root)

if __name__ == '__main__':
    main()
