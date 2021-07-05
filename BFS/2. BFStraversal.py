from collections import deque


class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self, data=None):
        self.root = Node(data)

    def level_order(self):
        res = []
        if not self.root:
            return res

        q = deque()
        q.append(self.root)
        while q:
            level_size = len(q)
            level = []
            for _ in range(level_size):
                cnode = q.popleft()
                level.append(cnode.val)
                if cnode.left:
                    q.append(cnode.left)
                if cnode.right:
                    q.append(cnode.right)

            res.append(level)
        return res


t = Tree(1)
t.root.left = Node(2)
t.root.right = Node(3)
t.root.left.left = Node(4)
t.root.left.right = Node(5)
t.root.right.left = Node(6)
t.root.right.right = Node(7)

print(t.level_order())