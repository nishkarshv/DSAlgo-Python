def myPow(x, n):
    if n < 0 :
        n = -n
        x = 1/x
    i = n
    ans = 1
    cur_prod = x
    while i > 0:
        if i%2 == 1:
            ans = ans*cur_prod
        cur_prod = cur_prod*cur_prod
        i = i//2
    return ans

x = 2
n = 10
print(myPow(x,n))