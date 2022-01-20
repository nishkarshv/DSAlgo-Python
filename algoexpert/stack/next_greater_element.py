# Function that takes in an array of integers and returns a new array containing , at each index, 
# the next element in the input array that's greater than the element at that index in input array
# if no next value greater return -1
# input = [2,5,-3,-4,6,7,2]
# output = [5,6,6,6,7,-1,5]
import unittest
def nextGreaterElement(array):
    # Write your code here.
    res = [-1]*len(array)
    stack = []
    for i in range(2*len(array)):
        circularidx = i%len(array)
        print(circularidx)
        while len(stack)>0 and array[stack[len(stack)-1]] < array[circularidx]:
            top = stack.pop()
            print(top, circularidx)
            res[top] = array[circularidx]
        stack.append(circularidx)
    return res

class TestCase(unittest.TestCase):
    def test_case_1(self):
        input = [2,5,-3,-4,6,7,2]
        output = [5,6,6,6,7,-1,5]
        actual = nextGreaterElement(input)
        self.assertEqual(output, actual)
        

