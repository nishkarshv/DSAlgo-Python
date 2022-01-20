class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def getverticalorder(root, hd, m):
    
    if root is None:
        return
    if hd not in m:
        m[hd] = [root.val]
    else:
        m[hd].append(root.val)
    
    getverticalorder(root.left, hd-1, m)
    getverticalorder(root.right, hd+1, m)


def verticalTraversal_notcorrect(root):
    ans = []
    hd = 0
    m = dict()
    getverticalorder(root, hd, m)
    for k,v in sorted(m.items()):
        ans.append(v)
    return ans

def verticalTraversal_level(root):
    ans = []
    # base case
    if root is None:
        return []
    # create empty queue
    q = []
    m = {}
    # map to store horizontal distance of nodes
    hd ={}
    q.append(root)
    hd[root] = 0
    m[0] = [root.val]
    # loop while q is not empty
    while len(q)>0:
        # dequeue node from q
        temp = q.pop(0)
        if temp.left:
            q.append(temp.left)
            hd[temp.left] = hd[temp]-1
            hdist = hd[temp.left]
            if m.get(hdist) is None:
                m[hdist] = []
            m[hdist].append(temp.left.val)
        if temp.right:
            q.append(temp.right)
            hd[temp.right] = hd[temp]+1
            hdist = hd[temp.right]
            if m.get(hdist) is None:
                m[hdist] = []
            m[hdist].append(temp.right.val)
    for k,v in sorted(m.items()):
        ans.append(v)
    return ans
import collections
def verticalTraversal(root):
    ans = []
        # base case
    if root is None:
        return
    q = []
    q.append((root,0))
    d = collections.defaultdict(list)
    while q:
        d1 = collections.defaultdict(list)
        print(d)
        for _ in range(len(q)):
            node,level  = q.pop(0)
            d1[level].append(node.val)
            if node.left:
                q.append((node.left, level-1))
            if node.right:
                q.append((node.right, level+1))
        #print(d1)
        for k in d1:
            #print(k, d[k],d1[k])
            d[k].extend(sorted(d1[k]))
        #print(d)
    ans = [d[k] for k in sorted(d)]
    return ans
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.right.left = Node(6) 
root.right.right = Node(7) 
root.right.left.right = Node(8) 
root.right.right.right = Node(9) 

print(verticalTraversal(root))