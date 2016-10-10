import numpy as np

from build_matrix import build_from_sets

S = {1, 2, 3, 4, 5}
A1 = {1, 5}
A2 = {2, 4}
A3 = {2, 3}
A4 = {3}
A5 = {1, 4, 5}
sets = [A1, A2, A3, A4, A5]
grid = build_from_sets(S, sets)

print grid
