class TreeNode:
    def __int__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def flattentree(root: TreeNode):
    if not root:
        return None
    if not root.left and not root.right:
        return root
    lefttail = flattentree(root.left)
    righttail = flattentree(root.right)
    if lefttail:
        lefttail.right = root.right
        root.right = root.left
        root.left = None
    return righttail if righttail else lefttail

def flatten(root:TreeNode):
    flattentree(root)
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(flatten(root))