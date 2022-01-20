# Write a function that takes in a string made up of brackets ((,), [,],{,}) and other optional characters. Function should return boolean whether string is balanced with regards to brackets
# constraint - brackets cannot overlap each other like [(]).
# sample input - "([])(){}(())()()"
# sample output - true // balanced


import unittest

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(balancedBrackets("([])(){}(())()()"), True)


def balancedBrackets(string):
    openingbrackets = "({["
    closingbrackets = ")}]"
    bracketsdict = {
        ")":"(",
        "}":"{",
        "]":"["
    }
    stack = []
    for char in string:
        if char in openingbrackets:
            stack.append(char)
        elif char in closingbrackets:
            if len(stack) == 0:
                return False
            if stack[-1] == bracketsdict[char]:
                stack.pop()
            else:
                return False
    return len(stack) == 0
    
