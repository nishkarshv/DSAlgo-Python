'''
Example 1:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: 
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.

Example 2:

Input: tasks = ["A","A","A","B","B","B"], n = 0
Output: 6
Explanation: On this case any permutation of size 6 would work since n = 0.
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
...
And so on.

'''
class Solution:
    def leastInterval(self, tasks, n: int) -> int:
        frequency = [0]*26
        for t in tasks:
            frequency[ord(t) - ord('A')]+=1
        frequency.sort()
        f_max = frequency.pop()
        idle_time = (f_max-1)*n
        while frequency and idle_time >0 :
            idle_time-=min(f_max-1, frequency.pop())
        idle_time = max(0, idle_time)
        return idle_time+len(tasks)
sol = Solution()
tasks = ["A","A","A","B","B","B"]
n = 2

print(sol.leastInterval(tasks, n))