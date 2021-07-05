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
    def nodeToDigitSum(self):
        if not self.root:
            return 0
        if self.root and not self.root.left and not self.root.right:
            return self.root.val

        return self._fun(self.root, 0)

    def _fun(self, cnode, total):
        if cnode is None:
            return 0
        total = 10 * total + cnode.val
        if cnode.left is None and cnode.right is None:
            return total
        return self._fun(cnode.left, total) + self._fun(cnode.right, total)


# t = Tree(1)
# t.root.left = Node(2)
# t.root.right = Node(3)
# t.root.left.left = Node(4)
# t.root.left.right = Node(5)
# t.root.right.left = Node(6)
# t.root.right.right = Node(7)

t = Tree(1)
t.root.left = Node(7)
t.root.right = Node(9)
t.root.right.left = Node(2)
t.root.right.right = Node(9)

print(t.nodeToDigitSum())