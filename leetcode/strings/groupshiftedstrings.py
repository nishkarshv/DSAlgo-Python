'''
Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

"abc" -> "bcd" -> ... -> "xyz"

Given a list of non-empty strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

Example:

Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
Output: 
[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]

'''
import collections
def groupstrings(strings):
    sdict = collections.defaultdict(str)
    for s in strings:
        key = ()
        for i in range(len(s)-1):
            diff = 26+ord(s[i+1]) -ord(s[i])
            key+=(diff%26,)
        sdict[key] = sdict.get(key, [])+[s]
    print(sdict)
    return list(sdict.values())
inputlist = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
print(groupstrings(inputlist))
inp = ["abc", 'al']
print(groupstrings(inp))