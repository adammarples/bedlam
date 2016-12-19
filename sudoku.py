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
    a new one provided as a text file."""

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
    return format_checker(path)

def save_as_sudoku(src):
    path, filename = os.path.split(src)
    name = os.path.splitext(filename)[0]
    dst = os.path.join(SUDOKU_TEXT_DIR, filename)
    shutil.copyfile(src, dst)
    return name


if __name__ == '__main__':
    for output in plac.call(main):
        print(output)
