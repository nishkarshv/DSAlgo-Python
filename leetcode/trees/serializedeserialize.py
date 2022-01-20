# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def rserialise(node, string):
            if node is None:
                string+="None,"
            else:
                string+=str(node.val)+","
                string = rserialise(node.left, string)
                string = rserialise(node.right, string)
            return string
        return rserialise(root, "")
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def rdeserialise(datalist):
            if datalist[0] == 'None':
                datalist.pop(0)
                return None
            root = TreeNode(datalist[0])
            datalist.pop(0)
            root.left = rdeserialise(datalist)
            root.right = rdeserialise(datalist)
            return root
        data_list = data.split(",")
        root = rdeserialise(data_list)
        return root
        

# Your Codec object will be instantiated and called as such:
ser = Codec()
deser = Codec()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)
ans = deser.deserialize(ser.serialize(root))
print(ans)