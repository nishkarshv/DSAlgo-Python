'''
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]
'''
'''
Algorithm

Following the above intuition, it seems intuitive to implement the solution with recursion.

We define a recursive function called _wordBreak_topdown(s) which generates the results for the input string. Here are a few steps to implement our recursive function.

    First of all, as the base case of the recursion, when the input string is empty, 
    the recursion would terminate. Note that we return a list of empty list as the result, rather than just an empty list.

    As the main body of the function, we run an iteration over all the prefixes of the input string.
     If the corresponding prefix happens to match a word in the dictionary, we then invoke recursively the function on the postfix.

    At the end of the iteration, we keep the results in the hashmap named memo with each valid postfix string 
    as its key and the list of words that compose the prefix of as the value. For instance, for the postfix dogo, its corresponding entry in the hashmap would be memo["dogo"] = ["do", "go"].

    Finally, as the result, we return the entry of memo with the input string as the key. (The string itself is a postfix of the string itself.)

'''
from collections import defaultdict, Counter
class Solution:
    def wbhelper(self, s, wordDict, memo):
        if s in memo:
            return memo[s]
        if not s:
            return []
        res = []
        for word in wordDict:
            if not s.startswith(word):
                continue
            if len(word) == len(s):
                res.append(word)
            else:
                resofrest = self.wbhelper(s[len(word):], wordDict, memo)
                for item in resofrest:
                    item = word +' ' + item
                    res.append(item)
        memo[s] = res
        print(memo)
        return res
    def wordBreak(self, s: str, wordDict):
        return self.wbhelper(s, wordDict, {})
class Solution_dp:
    def wordBreak(self, s: str, wordDict):
        # def sentences(i):
        #     if i not in memo:
        #         memo[i] = [s[i:j] + (tail and ' ' + tail)
        #         for j in range(i+1, len(s)+1)
        #             if s[i:j] in wordDict
        #                for tail in sentences(j)]
        #     return memo[i]
        # return sentences(0)
    
        if set(Counter(s).keys()) > set(Counter("".join(wordDict)).keys()):
            return []
        
        s_length = len(s) + 1
        dp = [ [] for _ in range(s_length)]
        dp[0] = ['']
        
        word_set = set(wordDict)
        for i in range(1, s_length):
            sublist = []
            for j in range(i):
                if s[j:i] in word_set and dp[j]:
                    for subsentence in dp[j]:
                        sublist.append((subsentence + ' ' + s[j:i]))
            dp[i] = sublist
        print(dp)
        return [each[1:] for each in dp[-1]]
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
sol = Solution()
print(sol.wordBreak(s, wordDict))