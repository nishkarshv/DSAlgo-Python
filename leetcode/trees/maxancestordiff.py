class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def maxAncestorDiff(root):
    def dfs(node, high, low):
        if not node:
            return high - low
        high = max(high, node.val)
        low = min(low, node.val)
        return max(dfs(node.left, high, low), dfs(node.right, high,low))
    if not root:
        return 0
    return dfs(root, root.val, root.val)
def maxAncestorDiff_iter(root):
    maxval = float('-inf')
    stack = [(root, root.val, root.val)]
    while len(stack)>0:
        temp, curmax, curmin = stack.pop()
        if temp.val > curmax:
            curmax = temp.val
        if temp.val < curmin:
            curmin = temp.val
        if curmax - curmin > maxval:
            maxval = curmax - curmin
        if temp.left:
            stack.append((temp.left,curmax, curmin))
        if temp.right:
            stack.append((temp.right, curmax, curmin))
    return maxval

root = Node(8) 
root.left = Node(3) 
root.right = Node(10)  
root.left.left = Node(1)
root.left.right = Node(6)
root.left.right.left = Node(4)
root.left.right.right = Node(7)
root.right.right = Node(14)
root.right.right.left = Node(13) 

print(maxAncestorDiff(root))
print(maxAncestorDiff_iter(root))