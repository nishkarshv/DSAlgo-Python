'''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
'''
def searchrange(nums, target, left):
    low = 0
    high = len(nums)
    while low < high:
        mid = (low+high)//2
        if nums[mid] > target or (left and target == nums[mid]):
            high = mid
        else:
            low = mid+1
    return low
def searchRange(nums, target):
    
    leftidx = searchrange(nums, target, True)
    if leftidx == len(nums) or nums[leftidx] != target:
        return [-1,-1]
    res = [leftidx, searchrange(nums, target, False)-1]
    return res

#nums = [5,7,7,8,8,10]
#target = 8
nums = [1]
target = 1
print(searchRange(nums, target))