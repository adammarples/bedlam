#from linked_lists import root_as_grid

def search(root, k, solutions):

    #print ('k', k)
    if root == root.r:
        print ('Solution found', [n.name[0] for n in solutions])#print solution
        return solutions
    c = pick_column(root)
    #print ('Covering', c.name)
    cover_column(c)

    node = c.d
    while node is not c:
        #print ('down to', node.name, '(append)')
        solutions.append(node)#Ok

        rnod = node.r
        while rnod is not node:
            #print ('right to', rnod.name)
            cover_column(rnod.c)
            rnod = rnod.r

        search(root, k+1, solutions)
        #print ('k', k)
        #node = solutions[k-1]#??
        #node = solutions[k-1]#??
        node = solutions.pop()#??
        #print ('node from solutions', k, node.name)
        #print (node.name)

        c = node.c
        #print ('c picked as', c.name)

        lnod = node.l
        while lnod is not node:
            #print ('left to', lnod.name)
            uncover_column(lnod.c)
            lnod = lnod.l

        node = node.d

    uncover_column(c)


def run_solver(root):
    k = 0
    solutions = []
    search(root, k, solutions)


def pick_column(root):
    # Pick a column deterministically
    s = 1e6
    c = root
    #print ('c', c.name)
    node = root.r
    #print ('node', node.name)
    while node is not root:
        #print ('node', node.name)
        if node.s < s:
            #print ('new minimum', node.s, s, node.name)
            c = node
            s = node.s
        node = node.r
    return c

def cover_column(c):
    # "Cover" column c
    #print ('cover horizontally', c.name)
    c.remove_horiz()
    node = c.d
    while node is not c:
        rnod = node.r
        #print (node, rnod)
        while rnod is not node:
            #print ('cover vertically', rnod.name)
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
    name = 'example'
    grid = load('{}.csv'.format(name))
    print ('Load', name, '>', grid.shape)
    root = link_a_grid(grid)
    run_solver(root)

if __name__ == '__main__':
    main()
