'''
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

    The length of both num1 and num2 is < 5100.
    Both num1 and num2 contains only digits 0-9.
    Both num1 and num2 does not contain any leading zero.
    You must not use any built-in BigInteger library or convert the inputs to integer directly.

'''

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        diff = len(num1)-len(num2)
        num2 = "0"*diff+num2
        res = []
        carry = 0
        p1 = len(num1)-1
        p2 = len(num2)-1
        while p1>=0 and p2>=0:
            x1 = ord(num1[p1]) - ord('0') if p1>=0 else 0
            x2 = ord(num2[p2]) - ord('0') if p2>=0 else 0
            val = (x1+x2+carry)%10
            carry = (x1+x2+carry)//10
            res.append(val)
            p1-=1
            p2-=1
        if carry:
            res.append(carry)
        return ''.join(str(x) for x in res[::-1])
        
num1 = "123"
num2 = "23"
print(Solution().addStrings(num1,num2))