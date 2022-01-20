# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    def largestBSTSubtree_another(self, root):
        MAX_INT = float('inf')
        MIN_INT = float('-inf')
        if root is None:
            return 0, MIN_INT, MAX_INT, 0 , True
        if (root.left == None and root.right == None):
            return 1, root.val, root.val, 1, True
        l = self.largestBSTSubtree_another(root.left)
        r = self.largestBSTSubtree_another(root.right)
        ret = [0,0,0,0,0]
        ret[0] = (1+l[0]+r[0])
        if l[4] and r[4] and l[1] < root.val and r[2] > root.val:
            ret[2] = min(l[2], min(r[2], root.val))
            ret[1] = max(r[1], max(l[1], root.val))
            ret[3] = ret[0]
            ret[4] = True
            return ret
        ret[3] = max(l[3], r[3])
        ret[4] = False
        return ret
    def largestBSTSubtree_2(self, root):
        return self.largestBSTSubtree_another(root)[3]
    def largestBSTSubtree(self, root: TreeNode) -> int:
        def dfs(root):
            if not root:
                return 0,0 ,float('inf'),float('-inf')
            N1,n1,min1, max1 = dfs(root.left)
            N2,n2, min2, max2 = dfs(root.right)
            n = n1+1+n2 if max1<root.val<min2 else float('-inf')
            return max(N1,N2,n),n,min(min1, root.val) , max(max2, root.val)
        return dfs(root)[0]
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(1)
root.left.right = TreeNode(8)
root.right.right = TreeNode(7)
print(Solution().largestBSTSubtree(root))
print(Solution().largestBSTSubtree_2(root))