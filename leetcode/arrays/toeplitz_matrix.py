'''
Input:
matrix = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]
Output: True
Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.
'''
class Solution:
    
    
    def isToeplitzMatrix(self, matrix) -> bool:
        # fcount = 0
        # tcount = 0
        # for i,row in enumerate(matrix):
        #     for j,col in enumerate(row):
        #         if matrix[i-1][j-1] == col or i==0 or j==0:
        #             tcount+=1
        #         else:
        #             fcount+=1
        # if tcount > 0 and fcount ==0:
        #     return True
        # elif tcount >0 and fcount>0:
        #     return False
        # else:
        #     return False
        return all(i==0 or j==0 or matrix[i-1][j-1]==val for i,row in enumerate(matrix) for j,val in enumerate(row))
matrix = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]
s = Solution()
print(s.isToeplitzMatrix(matrix))