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
    def minDepth(self):

        if not self.root:
            return 0
        minDepth = 0
        q = deque()
        q.append(self.root)
        while q:
            minDepth += 1
            popped_ele = q.popleft()

            if not popped_ele.left or not popped_ele.right:
                return minDepth
            if popped_ele.left:
                q.appendleft(popped_ele.left)
            if popped_ele.right:
                q.appendleft(popped_ele.right)


t = Tree(1)

t.root.left = Node(2)

print(t.minDepth())
t.root.right = Node(3)


t.root.left.left = Node(4)
t.root.left.right = Node(5)

print(t.minDepth())
t.root.right.left = Node(6)
t.root.right.right = Node(7)

print(t.minDepth())