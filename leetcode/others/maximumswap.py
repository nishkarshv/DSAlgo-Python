# Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get. 
#Example 1:

#Input: 2736
#Output: 7236
#Explanation: Swap the number 2 and the number 7.

def maximumswap_brutforce(num):
    numlist = list(str(num))
    res = numlist[:]
    for i in range(len(numlist)):
        for j in range(i+1, len(numlist)):
            numlist[i], numlist[j] = numlist[j], numlist[i]
            if numlist>res:
                res = numlist[:]
            numlist[i], numlist[j] = numlist[j], numlist[i]
    return int("".join(res))

def maximumswap(num):
    numslist = list(str(num))
    numsdict = {}
    for i in range(len(numslist)):
        numsdict[int(numslist[i])] = i
    for i in range(len(numslist)):
        for d in range(9,int(numslist[i]), -1):
            j = 0
            if d in numsdict:
                j = numsdict[d]
            if i<j:
                numslist[i], numslist[j] = numslist[j], numslist[i]
                return int("".join(numslist))
    #print(numsdict)
    return num
num = 9936
print(maximumswap(num))
  
class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = list(str(num))
        i = 0
        while i < len(nums)-1 and nums[i] >= nums[i+1]:
            i += 1
        if i == len(nums) - 1:
            return num
        k = i
        for j in range(len(nums)-1, i, -1):
            if nums[j] > nums[k]:
                k = j
        for j in range(i+1):
            if nums[j] < nums[k]:
                break
        nums[j], nums[k] = nums[k], nums[j]
        return int(''.join(nums))

def maximumswap_correct(num):
    A = list(str(num))
    last = {int(x): i for i, x in enumerate(A)}
    print(A, last)
    for i, x in enumerate(A):
        for d in range(9, int(x), -1):
            x = 0
            if d in last:
                x = last[d]
            print(last.get(d, 0),i,d, x)
            
            if x > i:
                A[i], A[last[d]] = A[last[d]], A[i]
                return int("".join(A))
    return num