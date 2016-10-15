import shape_reader
import coordinate_handler as co
import string
import numpy as np

np.set_printoptions(linewidth=150)

def build_from_txt(shape_file, n_shapes, box_size):
    # Load shapes
    shape_dict = shape_reader.read(shape_file, n_shapes, box_size)
    shape_reader.test(shape_dict, n_shapes, box_size)
    for shape_id, shape_array in shape_dict.items():
        # Convert Coords
        vector_list = co.vectors(shape_array, box_size)
        # Rotate, Do not rotate 1 shape for reducing mirror solutions
        rotation_list = co.rotate_shape(vector_list)
        # Recentre
        recentre_list = co.recentre_all(rotation_list)
        ## Reduce Once
        #reduced_list = co.reduce_all(recentre_list, box_size)
        ## Translate
        #translated_list = co.translate_all(reduced_list, box_size)
        ## Reduce Twice
        #rereduced_list = co.reduce_all(translated_list, box_size)
        # Translate
        translated_list = co.translate_all(recentre_list, box_size)
        # Convert to Grid
        converted_list = co.convert_all_to_grid(translated_list, box_size)
        # Array id grid
        array_id_vector = co.create_shape_grid_vector(shape_id, n_shapes)
        # Concatenate
        shape_grid = co.create_shape_grid(converted_list, array_id_vector)
        # Update shape_dict
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
    pass
