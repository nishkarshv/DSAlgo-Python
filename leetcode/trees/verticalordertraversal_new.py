class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

from collections import deque,defaultdict 
def verticalTraversal_bfs(root):
    columntable = defaultdict(list)
    q = deque([(root, 0)])
    while q:
        node, col = q.popleft()
        if node is not None:
            columntable[col].append(node.val)
            q.append((node.left, col-1))
            q.append((node.right, col+1))
    return [columntable[x] for x in sorted(columntable.keys())]

def verticalTraversal_dfs(root):
    if root is None:
        return []
    columntable = defaultdict(list)
    min_col = max_col = 0
    q = deque([(root,0)])
    while q:
        node, col = q.popleft()
        if node is not None:
            columntable[col].append(node.val)
            min_col = min(min_col, col)
            max_col = max(max_col, col)
            q.append((node.left, col-1))
            q.append((node.right, col+1))
    return [columntable[x] for x in range(min_col, max_col+1)]
root = Node(3) 
root.left = Node(9) 
root.right = Node(20)  
root.right.left = Node(15) 
root.right.right = Node(7)
print(verticalTraversal_bfs(root))
print(verticalTraversal_dfs(root))