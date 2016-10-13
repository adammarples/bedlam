

def run_solver(root):
    c = pick_column(root)
    cover_column(c)
    uncover_column(c)

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
    print (node.name)
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
    name = 'example'
    grid = load('{}.csv'.format(name))
    print ('Load', name, '>', grid.shape)
    root = link_a_grid(grid)
    run_solver(root)

if __name__ == '__main__':
    main()