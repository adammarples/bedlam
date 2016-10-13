

def run_solver(root):
    pass
    print (root)


def main():
    from main import load, link_a_grid
    name = 'example'
    grid = load('{}.csv'.format(name))
    print ('Load', name, '>', grid.shape)
    root = link_a_grid(grid)
    run_solver(root)

if __name__ == '__main__':
    main()
