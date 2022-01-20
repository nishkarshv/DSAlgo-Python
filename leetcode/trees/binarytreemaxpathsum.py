class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxpathsumutil(root):
    if not root:
        return 0
    left = maxpathsumutil(root.left)
    right = maxpathsumutil(root.right)
    cur_max = max(max(left, right)+root.val,root.val)
    maxtop = max(cur_max, left+right+root.val)
    maxpathsumutil.ans = max(maxpathsumutil.ans, maxtop)

    return cur_max

def maxPathSum_gfg(root):
    maxpathsumutil.ans = float('-inf')
    maxpathsumutil(root)
    return maxpathsumutil.ans

def maxPathSum(root):
    def maxpath(node):
        nonlocal max_val
        if not node:
            return 0
        left = maxpath(node.left)
        right = maxpath(node.right)
        firstmax = max(left, right) + node.val
        secondmax = max(firstmax, node.val)
        thirdmax = max(secondmax, left + right + node.val)
        max_val = max(max_val, thirdmax)
        return secondmax

    max_val = float('-inf')
    maxpath(root)
    return max_val
root = TreeNode(-10)
#root.left = TreeNode(-1)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(maxPathSum(root))
print(maxPathSum_gfg(root))