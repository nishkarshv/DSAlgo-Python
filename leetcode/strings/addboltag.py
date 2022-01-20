'''
Given a string s and a list of strings dict, you need to add a closed pair of bold tag <b> and </b> to wrap the substrings in s that exist in dict. 
If two such substrings overlap, you need to wrap them together by only one pair of closed bold tag. Also, if two substrings wrapped by bold tags are consecutive, 
you need to combine them.

Example 1:

Input: 
s = "abcxyz123"
dict = ["abc","123"]
Output:
"<b>abc</b>xyz<b>123</b>"
'''
class Solution:
    def addBoldTag(self, s: str, dict) -> str:
        status = [False]*len(s)
        ans = ""
        for word in dict:
            
            start = s.find(word)
            print(start)
            last = len(word)
            while start !=-1:
                for i in range(start, last+start):
                    status[i] = True
                start = s.find(word, start+1)
        i=0
        while i<len(s):
            if status[i]:
                ans+="<b>"
                while i < len(s) and status[i]:
                    ans+=s[i]
                    i+=1
                ans+="</b>"
            else:
                ans+=s[i]
                i+=1
                
        return ans
sol = Solution()
s = "abcxyz123"
dict = ["abc","123"]
print(sol.addBoldTag(s, dict))