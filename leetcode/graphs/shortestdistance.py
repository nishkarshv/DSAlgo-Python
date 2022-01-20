'''
317. Shortest Distance from All Buildings
Hard

You want to build a house on an empty land which reaches all buildings in the shortest amount of distance. You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:

    Each 0 marks an empty land which you can pass by freely.
    Each 1 marks a building which you cannot pass through.
    Each 2 marks an obstacle which you cannot pass through.

Example:

Input: [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]

1 - 0 - 2 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0

Output: 7 

Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2),
             the point (1,2) is an ideal empty land to build a house, as the total 
             travel distance of 3+3+1=7 is minimal. So return 7.
'''
'''
        Use hit to record how many times a 0 grid has been reached and use distSum to record the sum of distance from all 1 grids to this 0 grid.
         A powerful pruning is that during the BFS we use count1 to count how many 1 grids we reached. 
         If count1 < buildings then we know not all 1 grids are connected are we can return -1 
'''
import collections
class Solution:
    def shortestDistance(self, grid) -> int:
        m = len(grid)
        n = len(grid[0])
        if not grid or not grid[0]:
            return -1
        buildings = sum(val for line in grid for val in line if val == 1)
        hit = [[0]*n for _ in range(m)]
        distSum = [[0]*n for _ in range(m)]
        def bfs(x,y):
            visited = [[False]*n for _ in range(m)]
            visited[x][y] = True
            count1 = 1
            q = collections.deque([(x,y, 0)])
            while q:
                x,y,dist = q.popleft()
                for i, j in ((x+1,y),(x-1,y),(x,y-1),(x,y+1)):
                    if 0<=i<m and 0<=j<n and not visited[i][j]:
                        visited[i][j]= True
                        if not grid[i][j]:
                            q.append((i,j,dist+1))
                            hit[i][j]+=1
                            distSum[i][j]+=(dist+1)
                        elif grid[i][j]==1:
                            count1+=1
                            
            return count1 == buildings
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    if not bfs(i,j):
                        return -1
        return min([distSum[i][j] for i in range(m) for j in range(n) if not grid[i][j] and hit[i][j] == buildings] or [-1])
                    
grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
print(Solution().shortestDistance(grid))