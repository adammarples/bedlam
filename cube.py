import plac
import os
import shutil

from bedlam import BOXES_DIR, TEXT_DIR, GRID_DIR, saved_dict
from bedlam.builder import build
from bedlam.build_matrix import save

@plac.annotations(
    new = plac.Annotation('New Cube', 'option', 'n'),
    arc = plac.Annotation('Archived Cube', 'option', 'a'),
    shapes = plac.Annotation('N shapes', 'option', 's',  type=int),
    dim = plac.Annotation('N dims', 'option', 'd', type=int),
)

def main(new, arc, shapes, dim):
    """Runs the bedlam solver on either an existing cube or
a new one provided as a text file.

If solving an existing cube try running on bedlam, coffin, hoffmann
nob, soma or slothouber-graatsma.

If adding a new cube provide a txt file formatted like the following.

# Shape 1
0,0,0,0
0,0,1,0
1,1,1,0
0,1,0,0
#
0,0,0,0
0,0,0,0
0,0,0,0
0,0,0,0
#
0,0,0,0
0,0,0,0
0,0,0,0
0,0,0,0
#
0,0,0,0
0,0,0,0
0,0,0,0
0,0,0,0
#
# Shape 2

etc...

Example usage:
    python cube.py -a bedlam
    python cube.py -n D:\\test.txt 7 3

test.txt should contain 7 shapes of 3x3x3 sides

Your test.txt will be saved and you will then be able to run
    "python cube.py -a test" in future.

"""

    if new and shapes and dim:
        shapes = int(shapes)
        dim = int(dim)
        yield '[not yet implemented] new={}'.format(new)
        name = save_as_cube(new)
        grid = build(name, shapes, dim)
        print (name, shapes, dim)
        print (grid)
        save(os.path.join(GRID_DIR, '{}.csv'.format(name)), grid)
    if arc:
        yield 'archived={}'.format(arc)
        if saved_checker(arc):
            sh, di = saved_dict[arc]
            build(arc, sh, di)
        else:
            yield (arc, 'is not a valid saved cube')

def saved_checker(name):
    """checks if the solution is a valid saved solution."""
    path = os.path.join(BOXES_DIR, '{}_box.txt'.format(name))
    return os.path.isfile(path)

def save_as_cube(src):
    path, filename = os.path.split(src)
    name = os.path.splitext(filename)[0]
    dst = os.path.join(TEXT_DIR, filename)
    shutil.copyfile(src, dst)
    return name


if __name__ == '__main__':
    for output in plac.call(main):
        print(output)
