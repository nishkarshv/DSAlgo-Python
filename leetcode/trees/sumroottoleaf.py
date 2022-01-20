# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        
        def preorder(node, res):
            nonlocal roottoleaf
            if node:
                res = res*10+node.val
                if not (node.left or node.right):
                    roottoleaf+=res
                preorder(node.left ,res)
                preorder(node.right, res)
        roottoleaf = 0
        preorder(root,0)
        return roottoleaf
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
print(Solution().sumNumbers(root))