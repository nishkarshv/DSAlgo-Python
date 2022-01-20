class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left

def rangeSumBST(root, L, R):
    if not root:
        return 0
    elif root.val < L:
        return rangeSumBST(root.right, L, R)
    elif root.val > R:
        return rangeSumBST(root.left, L, R)
    return root.val + rangeSumBST(root.left, L, R) + rangeSumBST(root.right, L, R)

def rangesumBST_iterative(root, L, R):
    ans = 0
    st = [root]
    while st:
        node = st.pop()
        if node:
            if L<=node.val<=R:
                ans+=node.val
            if L< node.val:
                st.append(node.left)
            if node.val < R:
                st.append(node.right)

    return ans
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(3)
root.left.right = Node(7)
root.right.right = Node(18)
l = 7
r = 15
print(rangeSumBST(root,l,r))
print(rangesumBST_iterative(root, l, r))