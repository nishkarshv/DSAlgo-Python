def addstrings(num1, num2):
    if len(num1) < len(num2):
        num1, num2 = num2, num1
    n = max(len(num1), len(num2))
    diff = len(num1) - len(num2)
    num2 = "0"*diff + num2
    carry = 0
    res = []
    i = len(num1)-1
    j = len(num2)-1
    while i>=0 or j>=0:
        x1 = ord(num1[i]) - ord('0') if i>=0 else 0
        x2 = ord(num2[i]) - ord('0') if j>=0 else 0
        value = (x1+x2+carry)%10
        carry = (x1+x2+carry)//10
        res.append(value)
        i-=1
        j-=1
    if carry:
        res.append(carry)

    return "".join(str(x) for x in res[::-1])
print(addstrings("124","456"))