'''
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

 

Example 2:

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

'''
'''
Brutefoce O(n2) and O(1)
For each possible palindrome center, let's expand our candidate palindrome on the interval [left, right] as long as we can. 
The condition for expanding is left >= 0 and right < N and S[left] == S[right]. That means we want to count a new palindrome S[left], S[left+1], ..., S[right].
    def countSubstrings(self, S):
        N = len(S)
        ans = 0
        for center in xrange(2*N - 1):
            left = center / 2
            right = left + center % 2
            while left >= 0 and right < N and S[left] == S[right]:
                ans += 1
                left -= 1
                right += 1
        return ans
'''

class Solution:
    '''
    Our loop invariants will be that center, right is our knowledge of the palindrome with the largest right-most boundary with center < i, 
    centered at center with right-boundary right. Also, i > center, and we've already computed all Z[j]'s for j < i.

When i < right, we reflect i about center to be at some coordinate j = 2 * center - i. 
Then, limited to the interval with radius right - i and center i, the situation for Z[i] is the same as for Z[j].

For example, if at some time center = 7, right = 13, i = 10, then for a string like A = '@#A#B#A#A#B#A#＄', 
the center is at the '#' between the two middle 'A''s, the right boundary is at the last '#', i is at the last 'B', and j is at the first 'B'.

Notice that limited to the interval [center - (right - center), right] (the interval with center center and right-boundary right), 
the situation for i and j is a reflection of something we have already computed. Since we already know Z[j] = 3, we can quickly find Z[i] = min(right - i, Z[j]) = 3.

Now, why is this algorithm linear? The while loop only checks the condition more than once when Z[i] = right - i.
 In that case, for each time Z[i] += 1, it increments right, and right can only be incremented up to 2*N+2 times.

Finally, we sum up (v+1) / 2 for each v in Z. Say the longest palindrome with some given center C has radius R. 
Then, the substring with center C and radius R-1, R-2, R-3, ..., 0 are also palindromes. Example: abcdedcba is a palindrome with center e, 
radius 4: but e, ded, cdedc, bcdedcb, and abcdedcba are all palindromes.

We are dividing by 2 because we were using half-lengths instead of lengths. For example we actually had the palindrome a#b#c#d#e#d#c#b#a, so our length is twice as big.
    '''
    def countSubstrings_manacher(self, s):
        
                
        def manacher(S):
            A = "@#"+"#".join(S)+"#$"
            Z = [0]*len(A)
            center = right = 0
            for i in range(1, len(A)-1):
                if i < right:
                    Z[i] = min(right-i, Z[2*center-i])
                while A[i+Z[i]+1] == A[i-Z[i]-1]:
                    Z[i]+=1
                if i+Z[i]>right:
                    center, right = i, i+Z[i]
         
            return Z
        return sum((v+1)//2 for v in manacher(s))
    def countSubstrings(self, s: str) -> int:
        n =len(s)
        res = 0
        for i in range(2*n-1):
            left = i//2
            right = left+i%2
            while left>=0 and right<n and s[left] == s[right]:
                res+=1
                left-=1
                right+=1
        return res

input = "abc"
print(Solution().countSubstrings(input))
print(Solution().countSubstrings_manacher(input))