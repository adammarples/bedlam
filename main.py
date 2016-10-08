import build_matrix as bx
import algorithm_x as ax

def build_soma():
    grid = bx.build_from_txt('soma.txt', 7, 3)
    bx.save('soma.csv', grid)

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
    bx.save('wiki_example.csv', grid)

def solve(csv_name):
    grid = ax.load(csv_name)
    print ('Load', csv_name, 'as', grid.shape)
    solution = ax.solve_once(grid)

if __name__ == '__main__':
    #build_wiki_example()
    #build_soma()
    solve('wiki_example.csv')
    solve('soma.csv')

    
