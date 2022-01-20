'''
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:

Input: nums = [1], k = 1
Output: [1]


'''
import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums, k: int) :
        # O(1)
        if k == len(nums):
            return nums
        #build a hashmap with freq
        # O(n)
        count = Counter(nums)
        # build the heap of top k frequent elements and convert it into an output array
        # O(nlogk)
        print(count)
        return heapq.nlargest(k, count.keys(), key = count.get)

nums = [1,1,1,2,2,3]
k = 6
print(Solution().topKFrequent(nums, k))