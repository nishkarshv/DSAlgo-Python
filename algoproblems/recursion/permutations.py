import unittest

def getPermutations(array):
    res = []
    permutatehelper(0, array, res)
    
    return res

def permutatehelper(i, array, res):
    if i == len(array) - 1:
        res.append(array[:])
    else:
        for j in range(i, len(array)):
            swap(array, i, j)
            permutatehelper(i+1, array, res)
            swap(array, i, j)
            

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]
    
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        perms = getPermutations([1, 2, 3])
        self.assertTrue(len(perms) == 6)
        self.assertTrue([1, 2, 3] in perms)
        self.assertTrue([1, 3, 2] in perms)
        self.assertTrue([2, 1, 3] in perms)
        self.assertTrue([2, 3, 1] in perms)
        self.assertTrue([3, 1, 2] in perms)
        self.assertTrue([3, 2, 1] in perms)