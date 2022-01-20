import collections
def subarraysum(nums, k):
    count = 0
    sums = 0
    d = dict()
    d[0] = 1
    for i in range(len(nums)):
        sums+=nums[i]
        count+=d.get(sums-k,0)
        d[sums] = d.get(sums,0)+1
    return count

def subarraysum_easy(nums, k):
    count = 0
    currsum = 0
    sum_dict = collections.defaultdict(int)

    for i in range(len(nums)):
        currsum+=nums[i]
        x = currsum - k
        if currsum == k:
            
            count+=1
            print(count, sum_dict)
        if x in sum_dict:
            count+=sum_dict[x]
            print(count, sum_dict)
        sum_dict[currsum]+=1
        print(sum_dict)
    return count
print(subarraysum([3,4,5,2,-3,1,4,2], 7))
print(subarraysum_easy([3,4,5,2,-3,1,4,2], 7))