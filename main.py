import build_matrix as bx
import algorithm_x as ax

def build_soma():
    grid = bx.build_from_txt('soma.txt', 7, 3)
    bx.save('soma.csv', grid)

def build_bedlam():
    grid = bx.build_from_txt('bedlam.txt', 13, 4)
    bx.save('bedlam.csv', grid)

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

def build_example():
    S = {1, 2, 3, 4, 5}
    A1 = {1, 5}
    A2 = {2, 4}
    A3 = {2, 3}
    A4 = {3}
    A5 = {1, 4, 5}
    sets = [A1, A2, A3, A4, A5]
    grid = bx.build_from_sets(S, sets)
    bx.save('example.csv', grid)
    
def solve(csv_name):
    grid = ax.load(csv_name)
    print ('Load', csv_name, 'as', grid.shape)
    print(grid)
    solution, level_dict = ax.solve_once(grid)
    level = max(level_dict.keys())
    print ('level', level)

if __name__ == '__main__':
    #build_wiki_example()
    #build_soma()
    #build_example()
    build_bedlam()
    #solve('wiki_example.csv')
    #solve('soma.csv')
    #solve('example.csv')
    solve('bedlam.csv')

    
