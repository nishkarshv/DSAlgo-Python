'''
536. Construct Binary Tree from String
Medium

You need to construct a binary tree from a string consisting of parenthesis and integers.

The whole input represents a binary tree. It contains an integer followed by zero, one or two pairs of parenthesis. The integer represents the root's value and a pair of parenthesis contains a child binary tree with the same structure.

You always start to construct the left child node of the parent first if it exists.

 

Example 1:

Input: s = "4(2(3)(1))(6(5))"
Output: [4,2,6,3,1,5]


Example 2:

Input: s = "4(2(3)(1))(6(5)(7))"
Output: [4,2,6,3,1,5,7]
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val= val
        self.left = left
        self.right = right
class Solution:
    def str2tree_rec(self, s):
        i = s.find('(')
        if i<0:
            return TreeNode(int(s)) if s else None
        bal = 0
        for j, c in enumerate(s):
            if c == '(':
                bal+=1
            if c== ")":
                bal-=1
            if j>i and bal==0:
                break
        
        root = TreeNode(int(s[:i]))
        root.left = self.str2tree_rec(s[i+1:j])
        root.right = self.str2tree_rec(s[j+2:-1])
        return root
    
    
    def str2tree(self, s):
        st = [TreeNode(0)]
        num = ''
        for i, c in enumerate(s):
            if c == '(':
                st.pop()
            elif c != ')':
                num+=c
                if i+1 == len(s) or not s[i+1].isdigit():
                    node = TreeNode(int(num))
                    if st[-1].left:
                        st[-1].right = node
                    else:
                        st[-1].left = node
                    st.append(node)
                    num = ''
        return st[0].left
                
s = "4(2(3)(1))(6(5))"
print(Solution().str2tree(s))
print(Solution().str2tree_rec(s))       