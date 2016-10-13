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
        self.head = Node(None, 'head')
        self.tail = self.head

    def add_to_tail(self, name):
        node = Node(self.head, name, left=self.tail)
        self.tail.r = node
        self.tail = node

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

class Node:
    def __init__(self, head, name, up=None, down=None, left=None, right=None):
        self.head = head
        self.name = name
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

def main():
    import algorithm_x as ax
    name = 'example'
    grid = ax.load('{}.csv'.format(name))
    n_rows, n_cols = grid.shape
    print(grid)
    lx_row = LinkedList()
    for col in range(n_cols):
        lx_row.add_to_tail(col)
    #lx_row.show()
    for x in lx_row.iterate():
        print (x.name)





if __name__ == '__main__':
    main()
