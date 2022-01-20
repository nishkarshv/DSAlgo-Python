import unittest


def maxPathSum(tree):
    maxpathbranch, maxsum = findmax(tree)
    return maxsum

def findmax(tree):
    if tree is None:
        return (0, float('-inf'))
    
    lsb, lsum = findmax(tree.left) 
    rsb, rsum = findmax(tree.right)
    maxsumchildbranch = max(lsb, rsb)
    value = tree.value
    maxsubbranch = max(maxsumchildbranch+value, value)
    maxtsum = max(maxsubbranch, value+lsb+rsb)
    maxpathsum = max(lsum, rsum, maxtsum)
    return (maxsubbranch, maxpathsum)

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        test = BinaryTree(1).insert([2, 3, 4, 5, 6, 7])
        self.assertEqual(maxPathSum(test), 18)


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, values, i=0):
        if i >= len(values):
            return
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            if current.left is None:
                current.left = BinaryTree(values[i])
                break
            queue.append(current.left)
            if current.right is None:
                current.right = BinaryTree(values[i])
                break
            queue.append(current.right)
        self.insert(values, i + 1)
        return self