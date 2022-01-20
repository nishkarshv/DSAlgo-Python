"""
# Definition for a Node.

"""
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
import collections
class Solution:
    def __init__(self):
        self.visited = {}
    def cloneGraph_dfs(self, node: 'Node') -> 'Node':
        if not node:
            return node
        if node in self.visited:
            return self.visited[node]
        clone_node = Node(node.val, [])
        self.visited[node] = clone_node
        if node.neighbors:
            clone_node.neighbors = [self.cloneGraph_dfs(n) for n in node.neighbors]
            
    def cloneGraph_bfs(self, node: 'Node') -> 'Node':
        if not node:
            return node
        visited = {}
        q = collections.deque([node])
        visited[node] = Node(node.val, [])
        while q:
            n = q.popleft()
            for neighbor in n.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val,[])
                    q.append(neighbor)
                visited[n].neighbors.append(visited[neighbor])
        return visited[node]
    
node1 = Node(1,2)
node2  = Node(2,3)
node3  = Node(3,4)
print(Solution().cloneGraph_dfs(node1))