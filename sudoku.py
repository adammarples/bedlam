import plac
import os
import shutil

from bedlam import sudoku, SUDOKUS_DIR, SUDOKU_TEXT_DIR

@plac.annotations(
    new = plac.Annotation('New Sudoku', 'option', 'n'),
    arc = plac.Annotation('Archived Sudoku', 'option', 'a'),
)

def main(new, arc):
    """Runs the sudoku solver on either an existing board or
a new one provided as a text file.

If solving an existing board try running on japanese, x or worstcase

If adding a new board provide a txt file formatted like the following.

. 2 . 4 . 3 7 . .
. . . . . . . 3 2
. . . . . . . . 4
. 4 . 2 . . . 7 .
8 . . . 5 . . . .
. . . . . 1 . . .
5 . . . . . 9 . .
. 3 . 9 . . . . 7
. . 1 . . 8 6 . .

Example usage:
    python sudoku.py -a japanese
    python sudoku.py -n D:\\test.txt

Your test.txt will be saved and you will then be able to run
    "python sudoku.py -a test" in future.

"""

    if new:
        #yield 'new={}'.format(new)
        name = save_as_sudoku(new)
        sudoku.solve_and_build(name)
    if arc:
        #yield 'archived={}'.format(arc)
        if saved_checker(arc):
            sudoku.solve_and_build(arc)
        else:
            yield (arc, 'is not a valid saved sudoku')

def saved_checker(name):
    """checks if the solution is a valid saved solution."""
    path = os.path.join(SUDOKUS_DIR, '{}_box.txt'.format(name))
    return os.path.isfile(path)

def save_as_sudoku(src):
    path, filename = os.path.split(src)
    name = os.path.splitext(filename)[0]
    dst = os.path.join(SUDOKU_TEXT_DIR, filename)
    shutil.copyfile(src, dst)
    return name


if __name__ == '__main__':
    for output in plac.call(main):
        print(output)
