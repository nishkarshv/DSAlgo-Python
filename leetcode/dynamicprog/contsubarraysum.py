def checkSubarraySum(nums, k):
    sum = 0
    hmap = {}
    hmap[0] = -1
    for i in range(len(nums)):
        print(sum)
        sum+=nums[i]
        if k !=0:
            sum = sum%k
        print(hmap)
        if sum in hmap:
            if i - hmap[sum] > 1:
                print(i, hmap[sum])
                return True
        else:
            hmap[sum] = i
    
    return False

nums = [23,2, 4, 6, 7]
k = 6
print(checkSubarraySum(nums, k))