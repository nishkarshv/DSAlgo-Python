def addOperators(num, target):
    N = len(num)
    ans = []
    def recurse(index, prev, cur, val, s):
        if index == N:
            if val == target and cur == 0:
                ans.append("".join(s[1:]))
            return
        cur = cur*10 + int(num[index])
        str_op = str(cur)
        if cur > 0:
            # no op recursion
            recurse(index+1, prev,cur,val, s)
        # addition
        s.append('+')
        s.append(str_op)
        recurse(index+1, cur, 0, val+cur, s)
        s.pop()
        s.pop()
        # can subtract or multiply if there are some previous operands
        if s:
            s.append('-')
            s.append(str_op)
            recurse(index+1, -cur, 0 , val-cur, s)
            s.pop()
            s.pop()
            s.append('*')
            s.append(str_op)
            recurse(index+1, cur*prev,0,val-prev+(cur*prev),s)
            s.pop()
            s.pop()
    recurse(0,0,0,0,[])
    return ans
num = "123"
target = 6
print(addOperators(num, target))