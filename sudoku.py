import plac
import bedlam.sudoku

@plac.annotations(
    new = plac.Annotation('New Sudoku', 'option', 'n'),
    arc = plac.Annotation('Archived Sudoku', 'option', 'a'),
)

def main(new, arc):
    """Runs the sudoku solver on either an existing board or
    a new one provided as a text file."""

    if new:
        yield 'new={}'.format(new)
    if arc:
        yield 'archived={}'.format(arc)


if __name__ == '__main__':
    for output in plac.call(main):
        print(output)
