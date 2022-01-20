import unittest

def powerset_iterative(array):
    subsets = [[]]
    for ele in array:
        for i in range(len(subsets)):
            currentsubset = subsets[i]
            subsets.append(currentsubset+[ele])
    print(subsets)
    return subsets

def powerset(array, idx=None):
    if idx is None:
        idx = len(array) - 1
    elif idx < 0:
        return [[]]
    ele = array[idx]
    subsets = powerset(array, idx-1)
    for i in range(len(subsets)):
        currentsubset = subsets[i]
        subsets.append(currentsubset + [ele])
    return subsets

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        output = list(map(lambda x: set(x),powerset([1, 2, 3])))
        self.assertTrue(len(output) == 8)
        self.assertTrue(set([]) in output)
        self.assertTrue(set([1]) in output)
        self.assertTrue(set([2]) in output)
        self.assertTrue(set([1, 2]) in output)
        self.assertTrue(set([3]) in output)
        self.assertTrue(set([1, 3]) in output)
        self.assertTrue(set([2, 3]) in output)
        self.assertTrue(set([1, 2, 3]) in output)
        
