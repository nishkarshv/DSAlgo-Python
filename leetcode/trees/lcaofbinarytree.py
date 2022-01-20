'''
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        # def __init__(self):
        #     self.ans = None
        if root is None:
            return None
        if root.val == p.val or root.val == q.val:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if (left and right) or (root in [p,q]):
            return root
        else:
            return left or right
    def lowestCommonAncestor_rec(self, root, p, q):
        # def __init__(self):
        #     self.ans = None
        self.ans = None
        def recurse(node):
            
            if not node:
                return False
            left = recurse(root.left)
            right = recurse(root.right)
            mid = node == p or node==q
            if mid+left+right >=2:
                self.ans = node
            return mid or left or right
     
        recurse(root)
        return self.ans

#root = [3,5,1,6,2,0,8,null,null,7,4]
p = TreeNode(5)
q = TreeNode(1)
root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
print(Solution().lowestCommonAncestor(root, p, q).val)