# Define MinMaxStack class for a min max stack. Class  should support:-
# Push and pop values on and off the stack
# Peek the top value of stack
# get minimum and maximum values in stack at any given point in time.

import unittest



        
class MinMaxStack:
    def __init__(self):
        self.minmaxstack = []
        self.stack = []
    
    def pop(self):
        self.minmaxstack.pop()
        return self.stack.pop()
        
    def peek(self):
        return self.stack[len(self.stack)-1]

    def push(self, value):
        minmaxdict = {
            "min": value,
            "max": value
        }
        if len(self.minmaxstack):
            last = self.minmaxstack[len(self.minmaxstack)-1]
            minmaxdict["min"] = min(last["min"], value)
            minmaxdict["max"] = max(last["max"], value)
        self.minmaxstack.append(minmaxdict)
        self.stack.append(value)
   
    def getMin(self):
        return self.minmaxstack[len(self.minmaxstack)-1]["min"]
    def getMax(self):
        return self.minmaxstack[len(self.minmaxstack)-1]["max"]
   
   
   
    

def testMinMaxPeek(self, min, max, peek, stack):
    self.assertEqual(stack.getMin(), min)
    self.assertEqual(stack.getMax(), max)
    self.assertEqual(stack.peek(), peek)

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        stack = MinMaxStack()
        stack.push(5)
        testMinMaxPeek(self, 5, 5, 5, stack)
        stack.push(7)
        testMinMaxPeek(self, 5, 7, 7, stack)
        stack.push(2)
        testMinMaxPeek(self, 2, 7, 2, stack)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 7)
        testMinMaxPeek(self, 5, 5, 5, stack)