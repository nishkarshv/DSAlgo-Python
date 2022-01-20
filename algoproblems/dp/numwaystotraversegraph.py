


import unittest

def numberOfWaysToTraverseGraph(width, height):
    numberofways = [[0 for _ in range(width+1)]for _ in range(height+1)]
    for i in range(1, width+1):
        for j in range(1, height+1):
            if i == 1 or j == 1:
                numberofways[j][i] = 1
            else:
                wleft = numberofways[j][i-1]
                wup = numberofways[j-1][i]
                numberofways[j][i] = wleft+wup
    return numberofways[height][width]

def numberOfWaysToTraverseGraph_rec(width, height):
    if width == 1 or height == 1:
        return 1
    return numberOfWaysToTraverseGraph_rec(height-1, width)+numberOfWaysToTraverseGraph_rec(height, width-1)
    
def numberOfWaysToTraverseGraph_fact(width, height):
    # sumofways = factorial((width-1) + (height-1))//factorial(width-1)*factorial(height-1)
    xd = width-1
    yd = height - 1
    nr = factorial(xd+yd)
    dr = factorial(xd)*factorial(yd)
    return nr//dr
    
def factorial(n):
    res = 1
    for i in range(2, n+1):
        res*=i
    return res

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        width = 4
        height = 3
        expected = 10
        actual = numberOfWaysToTraverseGraph_fact(width, height)
        self.assertEqual(actual, expected)

