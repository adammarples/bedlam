class LinkedList:
    """ To remove a, reroute parent and child for L and R
    R[L[a]] = R[a]
    L[R[a]] = L[a]

    To replace a, reroute parent and child for L and R back to a
    R[L[a]] = a
    L[R[a]] = a
    because a retains all its links

    """
    def __init__(self):
        self.header = ListHeader()
        self.members = []

    def add_to_tail(self):
        node = Node()
        if self.members == []:
            pass
        else:
            parent = self.members[-1]
            head = self.members[0]
            node.l = parent
            node.r = head
            parent.r = node
            head.l = node
        self.members.append(node)

    def remove_by_name(self, name):
        node = self.head
        while node.r is not None:
            pass

    def iterate(self, node=None):
        if node is None:
            node = self.head
            yield node
        while node is not self.tail:
            node = node.r
            yield node

class ListHeader:
    def __init__(self):
        pass

class Node:
    def __init__(self, c=None, up=None, down=None, left=None, right=None):
        self.c = c
        self.u = up
        self.d = down
        self.l = left
        self.r = right

    def remove(self):
        self.u.d = self.d
        self.d.u = self.u
        self.r.l = self.l
        self.l.r = self.r

    def reinsert(self):
        self.u.d = self
        self.d.u = self
        self.l.r = self
        self.r.l = self

class ColumnObject(Node):
    def __init__(self, name, size):
        super().__init__()
        self.name = name
        self.s = size
        print (self.__dict__)


def walk(grid):
    m, n = grid.shape
    for j in range(m):
        for i in range(n):
            if grid[i][j]:
                pass

def main():
    import algorithm_x as ax
    name = 'example'
    grid = ax.load('{}.csv'.format(name))
    n_rows, n_cols = grid.shape
    print(grid)
    column_list = LinkedList()

    for j in range(n_cols):
        column = grid.T[j]
        size = column.sum()
        ColumnObject(j, size)




if __name__ == '__main__':
    main()
