'''
Given a string S of '(' and ')' parentheses, we add the minimum number of parentheses ( '(' or ')', and in any positions ) so that the resulting parentheses string is valid.

Formally, a parentheses string is valid if and only if:

    It is the empty string, or
    It can be written as AB (A concatenated with B), where A and B are valid strings, or
    It can be written as (A), where A is a valid string.

Given a parentheses string, return the minimum number of parentheses we must add to make the resulting string valid.

 

Example 1:

Input: "())"
Output: 1

Example 2:

Input: "((("
Output: 3

'''
class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        flag = 0
        ans = 0
        for i in S:
            if i == "(":
                flag+=1
            else:
                flag -=1
            if flag == -1:
                ans+=1
                flag+=1
        return flag+ans
            

S = "()))(("
print(Solution().minAddToMakeValid(S))