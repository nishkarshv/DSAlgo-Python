from math import ceil
def smallestdivisor(nums, threshold):
    low, high = 1, max(nums)+1
    res = 0
    while low < high:
        m = (low+high)//2
        if check(m,nums, threshold):
            res = m
            high = m
        else:
            low = m+1
    return res

def check(m, nums, threshold):
    s = 0
    for x in nums:
        s+=ceil(x/m)
    return s<=threshold

def smallestdivisor_coco(nums, threshold):
    left = 1
    right = max(nums)
    while left < right:
        middle = (left+right)//2
        remain = 0
        for num in nums:
            remain += ceil(num/middle)
        if remain <= threshold:
            right = middle
        else:
            left = middle+1
    return right
print(smallestdivisor([1,2,5,9], 6))
print(smallestdivisor_coco([1,2,5,9], 6))