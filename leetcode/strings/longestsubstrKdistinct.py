from collections import OrderedDict
class Solution:
    '''
    Now one could write down the algortihm.

    Return 0 if the string is empty or k is equal to zero.
    Set both set pointers in the beginning of the string left = 0 and right = 0 and init max substring length max_len = 1.
    While right pointer is less than N:
        Add the current character s[right] in the hashmap and move right pointer to the right.
        If hashmap contains k + 1 distinct characters, remove the leftmost character from the hashmap and move the left pointer so that sliding window contains again k distinct characters only.
        Update max_len.
        
hashmap
 def lengthOfLongestSubstringKDistinct(self, s: 'str', k: 'int') -> 'int':
        n = len(s) 
        if k == 0 or n == 0:
            return 0
        
        # sliding window left and right pointers
        left, right = 0, 0
        # hashmap character -> its rightmost position 
        # in the sliding window
        hashmap = defaultdict()

        max_len = 1
        
        while right < n:
            # add new character and move right pointer
            hashmap[s[right]] = right
            right += 1

            # slidewindow contains 3 characters
            if len(hashmap) == k + 1:
                # delete the leftmost character
                del_idx = min(hashmap.values())
                del hashmap[s[del_idx]]
                # move left pointer of the slidewindow
                left = del_idx + 1

            max_len = max(max_len, right - left)

        return max_len

    '''
    
    '''
    Algorithm

Let's use ordered dictionary instead of standard hashmap to trim the algorithm from the approach 1 :

    Return 0 if the string is empty or k is equal to zero.
    Set both set pointers in the beginning of the string left = 0 and right = 0 and init max substring length max_len = 1.
    While right pointer is less than N:
        If the current character s[right] is already in the ordered dictionary hashmap -- delete it, to ensure that the first key in hashmap is the leftmost character.
        Add the current character s[right] in the ordered dictionary and move right pointer to the right.
        If ordered dictionary hashmap contains k + 1 distinct characters, remove the leftmost one and move the left pointer so that sliding window contains again k distinct characters only.
        Update max_len.

    '''
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        
        # window = {}
        window = OrderedDict()
        if not s or k ==0:
            return 0
        left = 0 
        right = 0
        max_len = 1
        # while right < len(s):
        #     window[s[right]] = right
        #     right+=1
        #     if len(window) == k+1:
        #         del_idx = min(window.values())
        #         del window[s[del_idx]]
        #         left = del_idx+1
        #     max_len = max(max_len, right-left) 
        while right< len(s):
            ch = s[right]
            if ch in window:
                del window[ch]
            window[ch] = right
            right+=1
            if len(window) == k+1:
                _, del_idx = window.popitem(last=False)
                left = del_idx+1
            max_len = max(max_len, right-left)
        return max_len
sol = Solution()
s = "eceba"
k = 2
print(sol.lengthOfLongestSubstringKDistinct(s, k))