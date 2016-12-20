import plac
import os
import shutil

from bedlam import builder, BOXES_DIR, TEXT_DIR

@plac.annotations(
    new = plac.Annotation('New Cube', 'option', 'n'),
    arc = plac.Annotation('Archived Cube', 'option', 'a'),
)

def main(new, arc):
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
    python cube.py -n D:\\test.txt

Your test.txt will be saved and you will then be able to run
    "python cube.py -a test" in future.

"""

    if new:
        yield 'new={}'.format(new)
        #name = save_as_sudoku(new)
        #builder.solve_and_build(name)
    if arc:
        yield 'archived={}'.format(arc)
        if saved_checker(arc):
            sudoku.solve_and_build(arc)
        else:
            yield (arc, 'is not a valid saved sudoku')

def saved_checker(name):
    """checks if the solution is a valid saved solution."""
    path = os.path.join(BOXES_DIR, '{}_box.txt'.format(name))
    return os.path.isfile(path)

def save_as_sudoku(src):
    path, filename = os.path.split(src)
    name = os.path.splitext(filename)[0]
    dst = os.path.join(TEXT_DIR, filename)
    shutil.copyfile(src, dst)
    return name


if __name__ == '__main__':
    for output in plac.call(main):
        print(output)
