class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left=left
        self.right=right
def isValidBST(root):
    res = []
    #return isBSTutil(root)
    isbstutilinorder(root, res)
    for i in range(1, len(res)):
        if res[i-1] >= res[i]:
            return False
    return True
def isBSTutil(node, minv=float('-inf'), maxv=float('inf')):
    if node is None:
        return True
    if node.val < minv or node.val > maxv:
        return False
    return (isBSTutil(node.left, minv, node.val-1) and isBSTutil(node.right, node.val+1, maxv))

def isbstutilinorder(root, res):
    if root is None:
        return
    isbstutilinorder(root.left, res)
    res.append(root.val)
    isbstutilinorder(root.right, res)



root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)
if isValidBST(root):
    print("valid")
else:
    print("not valid")
