from collections import deque


class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self, data=None):
        self.root = Node(data)

    def avgLevel(self):
        res = []
        if not self.root:
            return res

        q = deque()
        q.append(self.root)
        while q:
            level_len = len(q)
            total = 0
            for _ in range(level_len):
                popped_ele = q.popleft()
                total += popped_ele.val
                if popped_ele.left:
                    q.append(popped_ele.left)
                if popped_ele.right:
                    q.append(popped_ele.right)

            res.append(total / level_len)
        return res


t = Tree(1)
t.root.left = Node(2)
t.root.right = Node(3)

t.root.left.left = Node(4)
t.root.left.right = Node(5)
t.root.right.left = Node(6)
t.root.right.right = Node(7)

print(t.avgLevel())