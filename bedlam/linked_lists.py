from collections import defaultdict

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
        else:
            node.r = node
            node.l = node
        self.members.append(node)

    def add_vertically(self, node):
        if self.members != []:
            parent = self.members[-1]
            head = self.members[0]
            node.u = parent
            node.d = head
            parent.d = node
            head.u = node
        else:
            node.d = node
            node.u = node
        self.members.append(node)


class Node:
    def __init__(self, name=None, c=None, up=None, down=None, left=None, right=None):
        self.name = name
        self.c = c
        self.u = up
        self.d = down
        self.l = left
        self.r = right

    def remove_horiz(self):
        self.r.l = self.l
        self.l.r = self.r

    def remove_vert(self):
        self.u.d = self.d
        self.d.u = self.u

    def insert_vert(self):
        self.u.d = self
        self.d.u = self

    def insert_horiz(self):
        self.l.r = self
        self.r.l = self


class ColumnObject(Node):
    def __init__(self, name=None, size=None):
        super().__init__()
        self.s = size
        self.name = name
        self.c = self


def link_a_grid(grid):
    n_rows, n_cols = grid.shape
    node_dict = defaultdict(list)
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
                node_dict[i].append(node)
                node.c = col_obj
                col_list.add_vertically(node)
    # Now link Row Lists
    for row, node_list in node_dict.items():
        row_list = LinkedList()
        for node in node_list:
            row_list.add_horizontally(node)
    return root

if __name__ == '__main__':
    import algorithm_x as ax
    name = 'example'
    grid = ax.load('{}.csv'.format(name))
    root = link_a_grid(grid)
