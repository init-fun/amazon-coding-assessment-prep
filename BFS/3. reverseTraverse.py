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
    def reverseTravese(self):
        res = deque()
        if self.root is None:
            return res
        q = deque()
        q.append(self.root)
        while q:
            level_len = len(q)
            level_nodes = []
            for _ in range(level_len):
                popped_ele = q.popleft()
                level_nodes.append(popped_ele.val)
                if popped_ele.left:
                    q.append(popped_ele.left)
                if popped_ele.right:
                    q.append(popped_ele.right)
            res.appendleft(level_nodes)
        return res

    def reverse2(self):
        res = deque()
        if self.root is None:
            return res

        q = deque()
        q.append(self.root)
        while q:
            len_level = len(q)
            l_nodes = []
            for _ in range(len_level):
                popped_ele = q.popleft()
                l_nodes.append(popped_ele.val)
                if popped_ele.left:
                    q.append(popped_ele.left)
                if popped_ele.right:
                    q.append(popped_ele.right)
            res.appendleft(l_nodes)
        return res


t = Tree(1)
t.root.left = Node(2)
t.root.right = Node(3)
t.root.left.left = Node(4)
t.root.left.right = Node(5)
t.root.right.left = Node(6)
t.root.right.right = Node(7)

# print(t.reverseTravese())
print(t.reverse2())
