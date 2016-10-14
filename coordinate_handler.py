import numpy as np
import string

def rotate_shape(array):
    """ return a list of 6 rotations of shape array, including original array.

    """
    rotation_list = []
    for i in range(4):
        array = rotate_x(array)
        for j in range(4):
            array = rotate_y(array)
            rotation_list.append(array)
    array = rotate_z(array)
    for j in range(4):
        array = rotate_y(array)
        rotation_list.append(array)
    array = rotate_z(array)
    array = rotate_z(array)
    for j in range(4):
        array = rotate_y(array)
        rotation_list.append(array)
    return np.array(rotation_list)

def recentre(array):
    """ recentre an array on 0,0,0.

    """
    point1 = array[0]
    negative = np.negative(point1)
    array = np.array([x+negative for x in array])
    return array

def recentre_all(shape_list):
    return np.array([recentre(shape) for shape in shape_list])

def rotate_x(shape):
    return np.array([(x, -z, y) for (x, y, z) in shape])

def rotate_y(shape):
    return np.array([(z, y, -x) for [x, y, z] in shape])

def rotate_z(shape):
    return np.array([(-y, x, z) for [x, y, z] in shape])

def translate_shape(array, box_size):
    """ return a list of all translated allowed arrays.
        disallows some arrays.

    """
    translated_list = []
    box = np.ones((box_size, box_size, box_size))
    box_vectors = vectors(box, box_size)
    for box_vector in box_vectors:
        translated_shape = np.array([point+box_vector for point in array])
        flat = translated_shape.flatten()
        if max(flat) < box_size and min(flat) >= 0:
            translated_list.append(translated_shape)
    return translated_list

def translate_all(array_list, box_size):
    translated_list = []
    for array in array_list:
        shape_translations = translate_shape(array, box_size)
        translated_list.extend(shape_translations)
    return np.array(translated_list)

def box_notation(array, box_size):
    box = np.zeros((box_size, box_size, box_size))
    for vector in array:
        [x, y, z] = vector
        box[x][y][z] = 1
    return box

def vectors(array, box_size):
    vector_coords = []
    for x in range(box_size):
        for y in range(box_size):
            for z in range(box_size):
                if array[x][y][z]:
                    vector = np.array((x, y, z))
                    vector_coords.append(vector)
    return np.array(vector_coords)

def get_shape_index(shape_id):
    return string.ascii_uppercase.index(shape_id)

def get_shape_id(shape_index):
    return string.ascii_uppercase[shape_index]

def create_shape_grid_vector(shape_id, n_shapes):
    ind = get_shape_index(shape_id)
    vector = np.zeros(n_shapes)
    vector[ind] = 1
    return vector

def convert_to_grid(array, box_size):
    return box_notation(array, box_size).flatten()

def convert_all_to_grid(array_list, box_size):
    return [convert_to_grid(array, box_size) for array in array_list]

def convert_to_vector(flatgrid, box_size):
    array = np.array(flatgrid).reshape((box_size, box_size, box_size))
    return vectors(array, box_size)

def create_shape_grid(converted_list, array_id_vector):
    return np.array([np.append(grid_line, array_id_vector) for grid_line in converted_list])

def reduce_all(array_list, box_size):
    strings = []
    reduced_list = []
    #print (array_list[0], array_list[0].shape)
    grids = convert_all_to_grid(array_list, box_size)
    for grid in grids:
        strings.append(''.join([str(int(x)) for x in grid]))
    setted = set(strings)
    #print (len(strings), len(setted))
    grids = [[int(j) for j in x] for x in setted]
    for flatgrid in grids:
        vectors = convert_to_vector(flatgrid, box_size)
        reduced_list.append(vectors)
    return reduced_list

if __name__ == '__main__':
    pass
