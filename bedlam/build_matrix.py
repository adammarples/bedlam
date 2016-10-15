import shape_reader
import coordinate_handler as co
import string
import numpy as np

np.set_printoptions(linewidth=150)

def build_from_txt(shape_file, n_shapes, box_size):
    # Load shapes
    shape_dict = shape_reader.read(shape_file, n_shapes, box_size)
    shape_reader.test(shape_dict, n_shapes, box_size)
    total_list = []

    # shape id, shape as a box
    for shape_id, shape_array in shape_dict.items():
        #print (shape_id)
        #print (shape_array.shape)
        # list of vectors of points making up the shape
        vector_list = co.vectors(shape_array, box_size)
        #print (vector_list.shape)
        # list of these points as rotated 6 faces * 4 orientations = 24
        rotation_list = co.rotate_shape(vector_list)
        # Fix one shape to reduce complexity
        #if shape_id == 'A':
        #    rotation_list = rotation_list[0]
        #print (rotation_list.shape)
        # recentre these rotations on the (0, 0, 0) square
        recentre_list = co.recentre_all(rotation_list)
        #print (recentre_list.shape)
        # now translate these points around all n * n * n squares
        # they are also trimmed for any overlaps with box edges
        translated_list = co.translate_all(recentre_list, box_size)
        #print (translated_list.shape)
        # convert thsese vector points to a flattened box
        converted_list = co.convert_all_to_grid(translated_list, box_size)
        #print (converted_list.shape)
        # reduce copies simple
        converted_list = co.reduce_flattened(converted_list)
        #print (converted_list.shape)
        array_id_vector = co.create_shape_grid_vector(shape_id, n_shapes)
        shape_grid = co.create_shape_grid(converted_list, array_id_vector)
        shape_dict[shape_id] = shape_grid

    full_grid = np.concatenate([shape_dict[key] for key in sorted(shape_dict)])
    return full_grid

def build_from_sets(universe, sets):
    grid = np.zeros((len(sets), len(universe)))
    for j, space in enumerate(universe):
        for i, shape in enumerate(sets):
            if space in shape:
                grid[i][j] = 1
    return grid

def save(filepath, grid):
    print('Saving', filepath, grid.shape)
    print (grid)
    np.savetxt(filepath, grid, fmt='%d', delimiter=",")

if __name__ == '__main__':
    import os
    grid = build_from_txt(os.path.join('text', 'soma.txt'), 7, 3)
    #save(os.path.join('grids', 'soma.csv'), grid)
