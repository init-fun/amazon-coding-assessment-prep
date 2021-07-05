from collections import deque


class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self, data=None):
        self.root = Node(data)

    # write you function here
    def hasSequence(self, lst):
        if not self.root:
            return False

        return self._seqTraversal(self.root, lst)

    def _seqTraversal(self, cnode, lst):
        pass


t = Tree(1)
t.root.left = Node(2)
t.root.right = Node(3)
t.root.left.left = Node(4)
t.root.left.right = Node(5)
t.root.right.left = Node(6)
t.root.right.right = Node(7)

print(t.funname())