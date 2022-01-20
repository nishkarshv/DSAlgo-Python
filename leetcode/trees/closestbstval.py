class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder(root):
    return inorder(root.left) + [root.val]+ inorder(root.right) if root else []
def closestvalue(root, target):
    #O(n) +O(n)
    l = inorder(root)
    return min(l,key=lambda x: abs(target-x))


def closestvalue_2(root,target):
    #O(n)+O(1)
    closest = root.val
    while root:
        closest = min(root.val, closest, key=lambda x: abs(target-x))
        root = root.left if target<root.val else root.right
    return closest

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(5)
root.right.right = Node(4)
target = 3.71
print(closestvalue(root, target))
print(closestvalue_2(root, target))