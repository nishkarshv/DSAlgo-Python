'''
1424. Diagonal Traverse II
Medium
Given a list of lists of integers, nums, return all elements of nums in diagonal order as shown in the below images.

 

Example 1:

Input: nums = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,4,2,7,5,3,8,6,9]


'''
import collections
class Solution:
    def findDiagonalOrder_dict(self, nums):
        d = collections.defaultdict(list)
        nrow = len(nums)
        for i in range(nrow):
            for j in range(len(nums[i])):
                d[i+j].append(nums[i][j])
        res = []
        for k in sorted(d.keys()):
            res.extend(d[k][::-1])
        return res
    def findDiagonalOrder_2(self, nums):
        res = []
        
        nrow = len(nums)
        for i in range(nrow):
            for j in range(len(nums[i])):
                res.append((i+j, j, nums[i][j]))
        print(res)
        res.sort()
        print(res)
        #print(res)
        return [x[2] for x in res]
    def findDiagonalOrder(self, nums):
        
        res = []
        for i, r in enumerate(nums):
            for j, c in enumerate(r):
                if len(res) <= i+j:
                    res.append([])
                res[i+j].append(c)
        return [a for r in res for a in reversed(r)]
                
            
s = Solution()
nums = [[1,2,3],[4,5,6],[7,8,9]]
print(s.findDiagonalOrder(nums))
print(s.findDiagonalOrder_2(nums))
print(s.findDiagonalOrder_dict(nums))