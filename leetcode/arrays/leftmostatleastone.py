'''
28. Leftmost Column with at Least a One
Medium

(This problem is an interactive problem.)

A binary matrix means that all elements are 0 or 1. For each individual row of the matrix, this row is sorted in non-decreasing order.

Given a row-sorted binary matrix binaryMatrix, return leftmost column index(0-indexed) with at least a 1 in it. If such index doesn't exist, return -1.

You can't access the Binary Matrix directly.  You may only access the matrix using a BinaryMatrix interface:

    BinaryMatrix.get(row, col) returns the element of the matrix at index (row, col) (0-indexed).
    BinaryMatrix.dimensions() returns a list of 2 elements [rows, cols], which means the matrix is rows * cols.

Submissions making more than 1000 calls to BinaryMatrix.get will be judged Wrong Answer.  Also, any solutions that attempt to circumvent the judge will result in disqualification.

For custom testing purposes you're given the binary matrix mat as input in the following four examples. You will not have access the binary matrix directly.
'''

'''
start in the top right corner, and if the current value is a 0, move down. If it is a 1, then move left.
You probably gained some intuitive sense as to why this works, just from watching the animation.

    When we encounter a 0, we know that the leftmost 1 can't be to the left of it.
    When we encounter a 1, we should continue the search on that row (move pointer to the left), in order to find an even smaller index.

'''
def leftmostcolumnwithone(matrix):
    res = 0
    rowlen = len(matrix)
    collen = len(matrix[0])
    i = 0
    j = collen-1
    while i< rowlen and j >=0:
        if matrix[i][j] == 0:
            i+=1
        else:
            j-=1
    res = j+1 if j != collen-1 else -1
    return res

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, cols = binaryMatrix.dimensions()
        smallest_index = cols
        for row in range(rows):
            # Binary Search for the first 1 in the row.
            lo = 0
            hi = cols - 1
            while lo < hi:
                mid = (lo + hi) // 2
                if binaryMatrix.get(row, mid) == 0:
                    lo = mid + 1
                else:
                    hi = mid
            # If the last element in the search space is a 1, then this row
            # contained a 1.
            if binaryMatrix.get(row, lo) == 1:
                smallest_index = min(smallest_index, lo)
        # If smallest_index is still set to cols, then there were no 1's in 
        # the grid. 
        return -1 if smallest_index == cols else smallest_index