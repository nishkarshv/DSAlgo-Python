class Node:
    def __init__(self, val=0, left = None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def depth(self, root):
        if not root:
            return 0
        l = self.depth(root.left)
        r = self.depth(root.right)
        self.ans = max(self.ans, l+r)
        return max(l,r)+1
    
    def diameterOfBinaryTree(self, root) -> int:
        self.ans = 0
        self.depth(root)
        return self.ans
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
s = Solution()
print(s.diameterOfBinaryTree(root))