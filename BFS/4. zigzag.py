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
    def zz(self):
        res = []
        if self.root is None:
            return res

        leftToRight = True
        q = deque()
        q.append(self.root)
        while q:
            level_length = len(q)
            level_nodes = deque()
            for _ in range(level_length):
                popped_ele = q.popleft()
                if leftToRight:
                    level_nodes.append(popped_ele.val)
                else:
                    level_nodes.appendleft(popped_ele.val)

                if popped_ele.left:
                    q.append(popped_ele.left)
                if popped_ele.right:
                    q.append(popped_ele.right)

            leftToRight = not leftToRight
            res.append(level_nodes)
        return res


t = Tree(1)
t.root.left = Node(2)
t.root.right = Node(3)
t.root.left.left = Node(4)
t.root.left.right = Node(5)
t.root.right.left = Node(6)
t.root.right.right = Node(7)

print(t.zz())