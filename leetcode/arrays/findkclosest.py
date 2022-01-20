'''
Given a sorted array arr, two integers k and x, find the k closest elements to x in the array. The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.

 

Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]

Example 2:

Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]

'''
'''
idea is to use binary search since list is sorted, 
Explanation

Assume we are taking A[i] ~ A[i + k -1].
We can binary research i
We compare the distance between x - A[mid] and A[mid + k] - x

@vincent_gui listed the following cases:
Assume A[mid] ~ A[mid + k] is sliding window

case 1: x - A[mid] < A[mid + k] - x, need to move window go left
-------x----A[mid]-----------------A[mid + k]----------

case 2: x - A[mid] < A[mid + k] - x, need to move window go left again
-------A[mid]----x-----------------A[mid + k]----------

case 3: x - A[mid] > A[mid + k] - x, need to move window go right
-------A[mid]------------------x---A[mid + k]----------

case 4: x - A[mid] > A[mid + k] - x, need to move window go right
-------A[mid]---------------------A[mid + k]----x------

If x - A[mid] > A[mid + k] - x,
it means A[mid + 1] ~ A[mid + k] is better than A[mid] ~ A[mid + k - 1],
and we have mid smaller than the right i.
So assign left = mid + 1.
'''
'''
Algorithm

The original array has been sorted so we can take this advantage by the following steps.

    If the target x is less or equal than the first element in the sorted array, the first k elements are the result.
    Similarly, if the target x is more or equal than the last element in the sorted array, the last k elements are the result.
    Otherwise, we can use binary search to find the index of the element, which is equal (when this list has x) or a little bit larger than x (when this list does not have it). 
    Then set low to its left k-1 position, and high to the right k-1 position of this index as a start. The desired k numbers must in this rang [index-k-1, index+k-1]. 
    So we can shrink this range to get the result using the following rules.
        If low reaches the lowest index 0 or the low element is closer to x than the high element, decrease the high index.
        If high reaches to the highest index arr.size()-1 or it is nearer to x than the low element, increase the low index.
        The looping ends when there are exactly k elements in [low, high], the subList of which is the result.

'''
class Solution:
    def findClosestElements(self, arr, k: int, x: int) :
        left = 0
        right = len(arr)-k
        while left < right:
            mid = (left+right)//2
            print(left, right, mid)
            print(x-arr[mid],arr[mid+k]-x)
            if x-arr[mid]>arr[mid+k]-x:
                left = mid+1
            else:
                right = mid
        return arr[left:left+k]
arr = [1,2,3,4,5]
k= 4
x = 3
print(Solution().findClosestElements(arr, k, x))

