from collections import  deque
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rightsideview_1(root):
    if root is None:
        return []
    next_level = deque([root,])
    rightside = []
    while next_level:
        curr_level = next_level
        next_level = deque()
        while curr_level:
            node = curr_level.popleft()
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        rightside.append(node.val)
    return rightside
def rightsideview_2(root):
    if root is None:
        return []
    rightside = []
    q = deque([root,])
    while q:
        level_len = len(q)
        for i in range(level_len):
            node = q.popleft()
            if i == level_len-1:
                rightside.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    return rightside
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(5)
root.right.right = Node(4)

print(rightsideview_1(root))
print(rightsideview_2(root))