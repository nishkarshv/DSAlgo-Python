'''
Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.

Example 1:

Input: S = "aab"
Output: "aba"

Example 2:

Input: S = "aaab"
Output: ""

'''
import heapq
class Solution:
    def reorganizeString_countmethod(self, S: str) -> str:
        n = len(S)
        A = []
        res = []
        for x in set(S):
            A.append((S.count(x),x))
        for c, x in sorted(A):
            if c > (n+1)/2:
                return ""
            res.extend(c*x)
        ans = [None]*n
        ans[::2], ans[1::2] = res[n//2:], res[:n//2]
        return "".join(ans)
    
    def reorganizeString(self, S: str) -> str:
        l = []
        n = len(S)
        for x in set(S):
            l.append((-S.count(x),x))
        heapq.heapify(l)
        if any(-nc > (len(S) + 1) / 2 for nc, x in l):
            return ""
        ans = []
        while len(l)>=2:
            n1, c1 = heapq.heappop(l)
            n2, c2 = heapq.heappop(l)
            ans.extend([c1, c2])
            if n1+1:
                heapq.heappush(l, (n1+1, c1))
            if n2+1:
                heapq.heappush(l, (n2+1, c2))
        return "".join(ans) + (l[0][1] if l else '')
S = "aabacc"
print(Solution().reorganizeString_countmethod(S))
print(Solution().reorganizeString(S))