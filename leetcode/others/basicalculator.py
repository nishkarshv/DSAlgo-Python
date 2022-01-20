'''
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7

Example 2:

Input: " 3/2 "
Output: 1

Example 3:

Input: " 3+5 / 2 "
Output: 5

'''
def calculate(s):
    if not s:
        return "0"
    stack = []
    num = 0
    sign = "+"
    for i in range(len(s)):
        if s[i].isdigit():
            num = num*10+ord(s[i]) -ord("0")
        if not s[i].isdigit() and not s[i].isspace() or i==len(s)-1:
            if sign == "-":
                stack.append(-num)
            elif sign == "+":
                stack.append(num)
            elif sign == "*":
                stack.append(stack.pop()*num)
            else:
                temp = stack.pop()
                if temp//num < 0 and temp%num != 0:
                    stack.append(temp//num+1)
                else:
                    stack.append(temp//num)
            sign = s[i]
            num = 0
    return sum(stack)
s = "3+2*2"    
print(calculate(s))

class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        stack = []
        sign = '+'
        num = 0
        for i, c in enumerate(s):
            if c.isdigit():
                num = num * 10 + int(c)
            if c in '+-*/' or i == len(s)-1:
                if sign == '*':
                    stack.append(stack.pop() * num)
                elif sign == '/':
                    p = stack.pop()
                    res = abs(p)//num
                    stack.append(res if p>0 else -res)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '+':
                    stack.append(num)
                sign = c
                num = 0
        
        return sum(stack)
        