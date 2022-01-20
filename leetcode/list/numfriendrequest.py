'''
Some people will make friend requests. The list of their ages is given and ages[i] is the age of the ith person. 

Person A will NOT friend request person B (B != A) if any of the following conditions are true:

    age[B] <= 0.5 * age[A] + 7
    age[B] > age[A]
    age[B] > 100 && age[A] < 100

Otherwise, A will friend request B.

Note that if A requests B, B does not necessarily request A.  Also, people will not friend request themselves.

How many total friend requests are made?

Example 1:

Input: [16,16]
Output: 2
Explanation: 2 people friend request each other.

Example 2:

Input: [16,17,18]
Output: 2
Explanation: Friend requests are made 17 -> 16, 18 -> 17.
'''
from collections import Counter
class Solution:
    def  numFriendRequests(self, ages) -> int:
        count = [0]*121
        for age in ages:
            count[age]+=1
        ans = 0
        for ageA, countA in enumerate(count):
            for ageB, countB in enumerate(count):
                if ageA*0.5+7>=ageB:
                    continue
                if ageA<ageB:
                    continue
                if ageA<100<ageB:
                    continue
                ans+=countA*countB
                if ageA==ageB:
                    ans-=countA
        return ans
    def numFriendRequests_counter(self, ages) -> int:
        count = Counter(ages)
        #print(count)
        ans = 0
        for k1,v1 in count.items():
            for k2, v2 in count.items():
                if k2 > 0.5*k1+7 and k2<=k1:
                    ans+=v1*v2
                if k1 == k2:
                    ans -= v1
        return ans
sol = Solution()
ages = [16,17,18]
print(sol.numFriendRequests(ages))