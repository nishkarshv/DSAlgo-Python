'''
 Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

    Any left parenthesis '(' must have a corresponding right parenthesis ')'.
    Any right parenthesis ')' must have a corresponding left parenthesis '('.
    Left parenthesis '(' must go before the corresponding right parenthesis ')'.
    '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
    An empty string is also valid.

Example 1:

Input: "()"
Output: True

Example 2:

Input: "(*)"
Output: True

Example 3:

Input: "(*))"
Output: True

'''

class Solution:
    def checkValidString(self, s: str) -> bool:
        l = 0
        h = 0
        for c in s:
            if c == "(":
                l+=1
            else:
                l-=1
            if c!=")":
                h+=1
            else:
                h-=1
            if h<0:
                break
            l = max(l,0)
        if l == 0:
            return True
        else:
            return False      
s = "(*)"
print(Solution().checkValidString(s))