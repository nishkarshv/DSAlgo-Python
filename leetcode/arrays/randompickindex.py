import random
def randompickindex(nums, target):
    count = 0
    ans = 0
    for i in range(len(nums)):
        if nums[i] == target:
            count+=1
            rand = random.randint(1, count)
            if rand == count:
                ans = i
    return ans

print(randompickindex([1,2,3,3,3], 3))

