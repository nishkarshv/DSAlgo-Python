'''
Input: nums1 = [1,0,0,2,3], nums2 = [0,3,0,4,0]
Output: 8
Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
v1.dotProduct(v2) = 1*0 + 0*3 + 0*0 + 2*4 + 3*0 = 8
'''
class SparseVector:
    def __init__(self, nums):
        self.seen = {}
        for i, x in enumerate(nums):
            if x:
                self.seen[i] = x

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        # sumval = 0
        # for i, x in self.seen.items():
        #     for j, y in vec.seen.items():
        #         if i == j:
        #             sumval+=(x*y)
        # return sumval
        ans = 0
        #case1: other vector is a sparse vector
        if len(self.seen) > len(vec.seen):
            for i in vec.seen:
                if i in self.seen:
                    ans += vec.seen[i] * self.seen[i]
        #case2: this vector is a sparse vector
        else:
            for i in self.seen:
                if i in vec.seen:
                    ans += vec.seen[i] * self.seen[i]
        return ans

# Your SparseVector object will be instantiated and called as such:
nums1 = [1,0,0,2,3]
nums2 = [0,3,0,4,0]
v1 = SparseVector(nums1)
v2 = SparseVector(nums2)
ans = v1.dotProduct(v2)
print(ans)