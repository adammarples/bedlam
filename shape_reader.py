import numpy as np
import string

np.set_printoptions(linewidth=250)

def read(filepath, n_shapes, box_size):
    """ return dictionary of shapes labeled A-Z from given text file.

    """
    with open(filepath) as data_file:
        array = np.loadtxt(data_file, dtype='int', delimiter=',').reshape((n_shapes,box_size,box_size,box_size))
        return {string.ascii_uppercase[i] : shape for i, shape in enumerate(array)}

def test(shape_dict, n_shapes, box_size):
    print('Testing Shapes')
    as_array = np.array(list(shape_dict.values()))
    assert as_array.sum() == box_size**3

if __name__ == '__main__':
    n_shapes = 7
    box_size = 3
    shape_dict = read('soma.txt', n_shapes, box_size)
    test(shape_dict, n_shapes, box_size)

