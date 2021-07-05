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
            return False

        if self.root.val == total and not self.root.left and not self.root.right:
            return True

        return self._checkPath(self.root, total)

    def _checkPath(self, cnode, total):
        if cnode:
            total -= cnode.val
            if total == 0:
                return True
            return self._checkPath(cnode.left, total) or self._checkPath(
                cnode.right, total
            )
        return False


t = Tree(1)
t.root.left = Node(2)
t.root.right = Node(3)
t.root.left.left = Node(4)
t.root.left.right = Node(5)
t.root.right.left = Node(6)
t.root.right.right = Node(7)

print(t.pathsum(8))