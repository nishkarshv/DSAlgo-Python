class Solution:
    def isMonotonic(self, A) -> bool:
        #return (all(A[i]<=A[i+1] for i in range(len(A)-1)) or all(A[i]>=A[i+1] for i in range(len(A)-1)))
    #other solution
        inc = True
        dec = True
        for i in range(len(A)-1):
            if A[i] > A[i+1]:
                inc = False
            if A[i] < A[i+1]:
                dec = False
        return inc or dec            
s = Solution()
A = [1,3,2]
print(s.isMonotonic(A))