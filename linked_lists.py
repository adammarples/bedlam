class LinkedList:
    """ To remove a, reroute parent and child for L and R
    R[L[a]] = R[a]
    L[R[a]] = L[a]

    To replace a, reroute parent and child for L and R back to a
    R[L[a]] = a
    L[R[a]] = a
    because a retains all its links

    """
    def __init__(self, head):
        self.head = head

class Node:
    def __init__(self, value=None, left=None, right=None):
        self.v = value
        self.l = left
        self.r = right

def main():
    import algorithm_x as ax
    name = 'example'
    grid = ax.load('{}.csv'.format(name))
    print(grid)
    head = Node()


if __name__ == '__main__':
    main()
