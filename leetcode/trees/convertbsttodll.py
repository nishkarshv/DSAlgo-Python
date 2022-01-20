
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def helper(node):
            nonlocal first, last
            if node:
                helper(node.left)
                if last:
                    last.right = node
                    node.left = last
                else:
                    first = node
                last = node
                helper(node.right)
        if not root:
            return None
        first, last = None, None
        helper(root)
        last.right = first
        first.left = last
        return first
    
    def treeToDoublyList_inorder(self, root: 'Node') -> 'Node': 
        if not root:
            return None
        
        def helper(node):
            l_res, r_res = node, node
            
            if node.left:
                l_head, l_tail = helper(node.left)
                l_res = l_head
                node.left = l_tail
                l_tail.right = node
                
            if node.right:
                r_head, r_tail = helper(node.right)
                r_res = r_tail
                node.right = r_head
                r_head.left = node
                
            return l_res, r_res
                
        head, tail = helper(root)
        
        head.left = tail
        tail.right = head
        
        return head
root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)
s = Solution()
print(s.treeToDoublyList_inorder(root))