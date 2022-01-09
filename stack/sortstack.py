# function that takes array of integers representing a stack, recursively sorts the stack in place (without creating new array)
# stack = [-5,2,-2,4,3,1]
# output = [-5,-2,1,2,3,4]

import unittest


def sortstack(stack):
    print(stack)
    if len(stack) == 0:
        return stack
    top = stack.pop()
    # print(top)
    sortstack(stack)
    insertinsortedorder(stack, top)
    return stack

def insertinsortedorder(stack, value):
    if len(stack) == 0 or stack[len(stack)-1]<=value:
        stack.append(value)
        return
    top = stack.pop()
    insertinsortedorder(stack, value)
    stack.append(top)
    print(top, stack)
    
    
    
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [-5,2,-2,4,3,1]
        output_prog = sortstack(input)
        print(output_prog)
        output =  [-5,-2,1,2,3,4]
        
        self.assertEqual(output, output_prog)