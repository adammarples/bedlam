import numpy as np

np.set_printoptions(linewidth=250)

def load(filepath):
    return np.loadtxt(filepath, delimiter=",")

name = 'bedlam'
grid = load('{}.csv'.format(name))
print ('Load', name, '>', grid.shape)

a = [216, 105, 485, 740, 535, 1289, 1534, 1755, 1392, 961, 904, 1110, 811]


x = np.take(grid, a, axis=0)
print(x)
print (x.sum(axis=0))
