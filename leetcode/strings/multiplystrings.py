def multiply(num1, num2):
    l1 = len(num1)
    l2 = len(num2)
    if l1 == 0  or l2 == 0:
        return "0"
    res = [0]*(l1+l2)
    for i,n1 in enumerate(reversed(num1)):
        for j,n2 in enumerate(reversed((num2))):
            x1 = ord(n1)-48
            x2 = ord(n2)-48
            mul = x1*x2
            res[i+j]+=mul
            res[i+j+1]+=res[i+j]//10
            res[i+j]%=10
    while len(res)>1 and res[-1]==0:
        res.pop()
    return ''.join(map(str,res[::-1]))



print(multiply("12","34"))