from collections import defaultdict
def findAnagrams(s,p):
    ns = len(s)
    np = len(p)
    if ns<np:
        return []
    p_count = [0]*26
    s_count = [0]*26
    for ch in p:
        p_count[ord(ch)-ord('a')]+=1
    output = []
    for i in range(ns):
        s_count[ord(s[i])-ord('a')]+=1
        if i >=np:
            s_count[ord(s[i-np]) - ord('a')]-=1
        if p_count == s_count:
            output.append(i-np+1)
    return output

def counter(s):
    d = defaultdict(int)
    for ch in s:
        d[ch]+=1
    return d

'''
Algorithm

    Build reference counter pCount for string p.

    Move sliding window along the string s:

        Recompute sliding window counter sCount at each step by adding one letter on the right and removing one letter on the left.

        If sCount == pCount, update the output list.
    return output
'''
from collections import Counter
def findAnagrams_2(s,p):
    # pcounter = counter(p)
    # scounter = counter(s[:len(p)-1])
    pcounter = Counter(p)
    scounter = Counter(s[:len(p)-1])
    print(pcounter,scounter)
    res = []
    for i in range(len(p)-1, len(s)):
        scounter[s[i]]+=1
        
        if scounter == pcounter:
            res.append(i-len(p)+1)
        print(scounter[s[i-len(p)+1]])
        scounter[s[i-len(p)+1]]-=1
        if scounter[s[i-len(p)+1]]==0:
            del scounter[s[i-len(p)+1]]
    return res
s= "cbaebabacd"
p = "abc"
print(findAnagrams(s,p))
print(findAnagrams_2(s,p))