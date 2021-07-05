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
    def successor(self, k):
        prev_node = None
        if not self.root:
            return prev_node
        res = []
        key_found = False
        q = deque()
        q.append(self.root)
        while q:
            popped_ele = q.popleft()
            cnode = popped_ele.val
            if key_found:
                return cnode
            if cnode == k:
                key_found = True

            if popped_ele.left:
                q.append(popped_ele.left)

            if popped_ele.right:
                q.append(popped_ele.right)


t = Tree(12)
t.root.left = Node(7)
t.root.right = Node(1)

t.root.left.left = Node(9)
# t.root.left.right = Node(5)
t.root.right.left = Node(10)
t.root.right.right = Node(5)

print(t.successor(9))