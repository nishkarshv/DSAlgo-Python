# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedListToBST_pointer(self, head):
        if not head:
            return
        if not head.next:
            return TreeNode(head.val)
        slow = head
        fast = head.next.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        tmp =slow.next
        slow.next = None
        root = TreeNode(tmp.val)
        root.left = self.sortedListToBST_pointer(head)
        root.right = self.sortedListToBST_pointer(tmp.next)
        return root
    def findsize(self, head):
        ptr = head
        c = 0
        while ptr:
            ptr = ptr.next
            c+=1
        return c
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        size = self.findsize(head)
        def convert(l, r):
            nonlocal head
            if l>r:
                return None
            mid = (l+r)//2
            left = convert(l, mid-1)
            node = TreeNode(head.val)
            node.left = left
            head = head.next
            right = convert(mid+1, r)
            node.right = right
            return node
        return convert(0, size-1)
head = ListNode(-10)
head.next = ListNode(-3)
head.next.next = ListNode(0)
head.next.next.next = ListNode(5)
head.next.next.next.next = ListNode(9)
print(Solution().sortedListToBST(head))