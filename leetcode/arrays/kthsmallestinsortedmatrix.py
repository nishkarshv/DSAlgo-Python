'''
Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.

'''
import heapq
'''

'''
class Solution:
    def kthSmallest(self, matrix, k: int) -> int:
        #heap approach
        n = len(matrix)
        minheap = []
        for i in range(min(k, n)):
            minheap.append((matrix[i][0], i, 0))
        heapq.heapify(minheap)
        while k:
            val, r, c = heapq.heappop(minheap)
            if c < n-1:
                heapq.heappush(minheap, (matrix[r][c+1], r, c+1))
            k-=1
        return val
    def countlessequal(self, matrix, mid, small, large):
        count = 0
        n = len(matrix)
        row = n-1
        col = 0
        while row>=0 and col<n:
            if matrix[row][col]> mid:
                large = min(large, matrix[row][col])
                row-=1
            else:
                small = max(small, matrix[row][col])
                count+=row+1
                col+=1
        return count, small, large
    def kthSmallest_binarysearch(self, matrix, k):
        #using binary search
        n = len(matrix)
        st = matrix[0][0]
        end = matrix[n-1][n-1]
        while st< end:
            mid = (st+end)//2
            smaller, larger = (matrix[0][0], matrix[n-1][n-1])
            count, smaller, larger = self.countlessequal(matrix, mid, smaller, larger)
            if count == k:
                return smaller
            if count <k:
                st = larger
            else:
                end = smaller  
        return st
matrix = [ [ 1,  5,  9],[10, 11, 13],[12, 13, 15]]
k = 8
print(Solution().kthSmallest(matrix,k))
print(Solution().kthSmallest_binarysearch(matrix, k))