from collections import defaultdict

class Node:
    """ To remove a, reroute parent and child for L and R
    R[L[a]] = R[a]
    L[R[a]] = L[a]

    To replace a, reroute parent and child for L and R back to a
    R[L[a]] = a
    L[R[a]] = a
    because a retains all its links

    """
    def __init__(self, name=None, c=None):
        self.name = name
        self.c = c
        self.u = self
        self.d = self
        self.l = self
        self.r = self

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

    def join_horiz(self, left):
        if left is None:
            return
        self.l = left
        left.r = self
        while left.l.r is not self:
            left = left.l
        self.r = left
        left.l = self

    def join_vert(self, up):
        if up is None:
            return
        self.u = up
        up.d = self
        while up.u.d is not self:
            up = up.u
        self.d = up
        up.u = self


class ColumnObject(Node):
    def __init__(self, name=None, size=None):
        super().__init__()
        self.s = size
        self.name = name
        self.c = self

def link_a_grid(grid):
    print ('Linking Grid')
    n_rows, n_cols = grid.shape
    node_dict = defaultdict(list)
    root = ColumnObject(name='root')
    # Make Column Lists
    current_column_node = root
    for j in range(n_cols):
        col = grid.T[j]
        col_obj = ColumnObject(name=j, size=col.sum())
        col_obj.join_horiz(current_column_node)
        current_row_node = col_obj
        for i in range(n_rows):
            if grid[i][j]:
                node = Node(name=(i, j))
                node_dict[i].append(node)
                node.c = col_obj
                node.join_vert(current_row_node)
                current_row_node = node
        current_column_node = col_obj
    # Now link Row Lists
    for row, node_list in node_dict.items():
        current_horiz_node = None
        for node in node_list:
            node.join_horiz(current_horiz_node)
            current_horiz_node = node
    print ('Done')
    return root


if __name__ == '__main__':
    pass
