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
        self.members = []

    def add_horizontally(self, node):
        if self.members != []:
            parent = self.members[-1]
            head = self.members[0]
            node.l = parent
            node.r = head
            parent.r = node
            head.l = node
        self.members.append(node)

    def add_vertically(self, node):
        if self.members != []:
            parent = self.members[-1]
            head = self.members[0]
            node.u = parent
            node.d = head
            parent.d = node
            head.u = node
        self.members.append(node)

    def iterate_horizontally(self):
        if self.members == []:
            return
        print( self.members)
        head = self.members[0]
        tail = self.members[-1]
        node = head
        while node is not tail:
            node = node.r
            yield node

class Node:
    def __init__(self, name=None, c=None, up=None, down=None, left=None, right=None):
        self.name = name
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
    def __init__(self, name=None, size=None):
        super().__init__()
        #print (self.__dict__)
        self.s = size
        self.name = name
        self.c = self

def iterate_vertically(c):
    node = c
    while node is not c.u:
        node = node.d
        yield node

def main():
    import algorithm_x as ax
    name = 'example'
    grid = ax.load('{}.csv'.format(name))
    n_rows, n_cols = grid.shape
    #print(grid)
    headers = LinkedList()
    root = ColumnObject(name='root')
    headers.add_horizontally(root)

    # Make Column Lists
    for j in range(n_cols):
        col = grid.T[j]
        col_obj = ColumnObject(name=j, size=col.sum())
        headers.add_horizontally(col_obj)
        col_list = LinkedList()
        col_list.add_vertically(col_obj)

        for i in range(n_rows):
            if grid[i][j]:
                node = Node(name=(i, j))
                node.c = col_obj
                col_list.add_vertically(node)

    # Now link Row Lists
    for c in headers.members[1:]:#skip root
        for x in iterate_vertically(c):
            print (c.name, x.name)



if __name__ == '__main__':
    main()
