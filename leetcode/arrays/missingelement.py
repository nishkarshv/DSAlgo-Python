'''
Given a sorted array A of unique numbers, find the K-th missing number starting from the leftmost number of the array.

Example 1:

Input: A = [4,7,9,10], K = 1
Output: 5
Explanation: 
The first missing number is 5.

Algorithm

    Implement missing(idx) function that returns how many numbers are missing until array element with index idx. Function returns nums[idx] - nums[0] - idx.

    Find an index such that missing(idx - 1) < k <= missing(idx) by a linear search.

    Return kth smallest nums[idx - 1] + k - missing(idx - 1).

'''
def missingElement(nums, k):
    missing = lambda idx: nums[idx] - nums[0] - idx  #nums[idx] = nums[0] + idx+k
    
    n = len(nums)
    if k > missing(n-1):
        return nums[-1]+k-missing(n-1)
    idx = 1
    while missing(idx) < k:
        idx+=1
    return nums[idx-1] + k - missing(idx-1)

def missingElement_binarysearch(nums, k):
    missing = lambda idx: nums[idx]-nums[0]-idx
    n  = len(nums)
    if k > missing(n-1):
        return nums[-1] + k - missing(n-1)
    left, right = 0, n-1
    while left != right:
        pivot = (left+right)//2
        if missing(pivot) < k:
            left = pivot+1
        else:
            right = pivot
    return nums[left-1] + k - missing(left-1)

A = [4,7,9,10]    
K = 3
print(missingElement(A, K))
print(missingElement_binarysearch(A,K))