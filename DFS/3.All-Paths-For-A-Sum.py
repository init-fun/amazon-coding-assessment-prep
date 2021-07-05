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
    def pathsum(self, total):
        if self.root is None:
            return 0
        c = 0
        count = self._checkPath(self.root, total, c)
        return count

    def _checkPath(self, cnode, total, count=0):
        if cnode:
            total -= cnode.val
            if total == 0:
                return count + 1
            if cnode.left:
                count = self._checkPath(cnode.left, total, count)
            if cnode.right:
                count = self._checkPath(cnode.right, total, count)

        return count


t = Tree(1)
t.root.left = Node(7)
t.root.right = Node(9)
t.root.left.left = Node(4)
t.root.left.right = Node(4)
t.root.right.left = Node(2)
t.root.right.right = Node(2)

print(t.pathsum(12))