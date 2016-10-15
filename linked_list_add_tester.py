import bedlam
from bedlam.linked_lists import LinkedList, ColumnObject, Node

def old_method():
    root = ColumnObject(name='root')
    headers = LinkedList()
    headers.add_horizontally(root)
    a = ColumnObject(name='a', size=1)
    headers.add_horizontally(a)
    b = ColumnObject(name='b', size=1)
    headers.add_horizontally(b)
    return root

def self_join(node):
    node.r = node
    node.l = node

def join_horiz(self, left):
    self.l = left
    left.r = self
    while left.l.r is not self:
        left = left.l
    self.r = left
    left.l = self

def new_method():
    Node.join_horiz = join_horiz
    root = ColumnObject(name='root')
    self_join(root)
    a = ColumnObject(name='a', size=1)
    self_join(a)
    b = ColumnObject(name='b', size=1)
    self_join(b)
    a.join_horiz(root)
    b.join_horiz(a)
    return root




def main():
    old = old_method()
    new = new_method()
    for x in range(4):
        print ((old.l.name, old.name, old.r.name), (new.l.name, new.name, new.r.name))
        old = old.r
        new = new.r


if __name__ == '__main__':
    main()
