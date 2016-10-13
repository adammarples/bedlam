import numpy as  np

np.set_printoptions(linewidth=250)

a = [408, 497, 745, 936, 1170, 70]#677
b = [408, 497, 745, 936, 1170, 70]#689

def load(filepath):
    return np.loadtxt(filepath, delimiter=",")

name = 'soma'
grid = load('{}.csv'.format(name))
print ('Load', name, '>', grid.shape)

print (np.take(grid, a, axis=0).sum(axis=0))
print (np.take(grid, b, axis=0).sum(axis=0))

print (grid[677])
print (grid[689])
