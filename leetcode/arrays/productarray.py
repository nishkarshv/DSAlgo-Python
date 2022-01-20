def productexceptself(nums):
    length = len(nums)
    L,R, res = [0]*length, [0]*length, [0]*length
    L[0] = 1
    for i in range(1, length):
        L[i] = nums[i-1] * L[i-1]
    R[length-1] = 1
    for i in reversed(range(length-1)):
        R[i] = nums[i+1] * R[i+1]
    for i in range(length):
        res[i] = L[i]*R[i]
    return res
def productexceptoptimized(nums):
    length = len(nums)
    ans = [0]*length
    ans[0] = 1
    for i in range(1, length):
        ans[i] = nums[i-1]*ans[i-1]
    R = 1
    for i in reversed(range(length)):
        ans[i] = ans[i]*R
        R *= nums[i]
    return ans

print(productexceptself([1,5]))
productexceptoptimized([1,2,3,4])