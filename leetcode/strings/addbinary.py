def addbinary(a, b):
    if len(a)<len(b):
        a,b = b,a
    n = max(len(a), len(b))
    diff = len(a) - len(b)
    b = '0'*diff+b
    res = []
    carry = 0
    for i in range(n-1, -1, -1):
        if a[i] == '1':
            carry+=1
        if b[i] == '1':
            carry+=1
        if carry%2 == 1:
            res.append('1')
        else:
            res.append('0')
        carry = carry//2
    if carry == 1:
        res.append('1')
    res.reverse()
    return ''.join(res)

print(addbinary('11','1'))