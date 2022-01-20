
import unittest
# O(2^n)
def getNthFib(N):
    if N == 0 or N == 1:
        return 0
    elif N == 2:
        return 1
    return getNthFib(N-1) + getNthFib(N-2)
# O(N), space O(1)
def getNthFib_Memoize(N):
    memoize = {1:0, 2:1}
    if N in memoize:
        return memoize[N]
    else:
        memoize[N] = getNthFib_Memoize(N-1) + getNthFib_Memoize(N-2)
    return memoize[N]
# O(N), space - O(1)
def getNthFib_optimize(N):
    
    lasttwo = [0, 1]
    for i in range(2, N):
        current = lasttwo[0] + lasttwo[1]
        lasttwo[0] = lasttwo[1]
        lasttwo[1] = current
    return lasttwo[1] if N > 1 else lasttwo[0]

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(getNthFib(6), 5)
    def test_case_2(self):
        self.assertEqual(getNthFib_Memoize(6), 5)
    def test_case_3(self):
        self.assertEqual(getNthFib_optimize(6), 5)