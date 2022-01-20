import unittest
# O(k^n) time | O(n) space
def staircaseTraversal_recursive(height, maxSteps):
    if height <= 1:
        return 1
    numofways = 0
    for step in range(1, min(height, maxSteps)+1):
        numofways += staircaseTraversal_recursive(height-step, maxSteps)
    return numofways
# O(k*n) -time| O(n) - space
def staircaseTraversal_dp(height, maxSteps):
    waystotop = [0 for _ in range(height+1)]
    waystotop[0] = 1
    waystotop[1] = 1
    for currentheight in range(2, height+1):
        step = 1
        while step <= maxSteps and step <= currentheight:
            waystotop[currentheight] = waystotop[currentheight] + waystotop[currentheight - step]
            step+=1
    return waystotop[height]
# O(k*n) -time| O(n) - space
def staircaseTraversal_itr1(height, maxSteps):
    memoize = {0:1, 1:1}
    if height in memoize:
        return memoize[height]
    numofways = 0
    for step in range(1, min(maxSteps, height)+1):
        numofways += staircaseTraversal_itr1(height-step, maxSteps)
    memoize[height] = numofways
    return numofways
# O(n) Time | O(n) space
def staircaseTraversal_itr2(height, maxSteps):
    currentnumofways = 0
    waystotop = [1]
    for currentheight in range(1, height+1):
        start = currentheight - maxSteps - 1 
        end =  currentheight - 1
        if start >= 0:
            currentnumofways -= waystotop[start]
        currentnumofways+=waystotop[end]
        waystotop.append(currentnumofways)
    return waystotop[height]

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        stairs = 4
        maxSteps = 2
        expected = 5
        actual = staircaseTraversal_recursive(stairs, maxSteps)
        self.assertEqual(actual, expected)

    def test_case_2(self):
        stairs = 4
        maxSteps = 2
        expected = 5
        actual = staircaseTraversal_dp(stairs, maxSteps)
        self.assertEqual(actual, expected)
        
    def test_case_3(self):
        stairs = 4
        maxSteps = 2
        expected = 5
        actual = staircaseTraversal_itr1(stairs, maxSteps)
        self.assertEqual(actual, expected)
        
    def test_case_4(self):
        stairs = 4
        maxSteps = 2
        expected = 5
        actual = staircaseTraversal_itr1(stairs, maxSteps)
        self.assertEqual(actual, expected)