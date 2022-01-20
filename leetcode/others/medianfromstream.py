'''
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.
For example,

[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

    void addNum(int num) - Add a integer number from the data stream to the data structure.
    double findMedian() - Return the median of all elements so far.

 

Example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2

'''
'''
we will maintain maxheap for lower numbers and minheap for higher numbers
if odd then max[0]
else average of roots of min[0] and max[0]
'''
import heapq
class MedianFinder:
    def __init__(self):
        self.minheap = []
        self.maxheap = []
    
    def addNum_alternative(self, num):
        if len(self.minheap) == 0:
            heapq.heappush(self.minheap, -num)
            return
        if num <= -self.minheap[0]:
            heapq.heappush(self.minheap, -num)
        else:
            heapq.heappush(self.maxheap, num)
        if len(self.minheap) - len(self.maxheap) == 2:
            heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))
        elif len(self.minheap) - len(self.maxheap) == -2:
            heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))
    
    def findMedian_alternative(self, num):
        if len(self.minheap) == len(self.maxheap):
            return (self.maxheap[0]-self.minheap[0])/2.0
        return -float(self.minheap[0]) if len(self.minheap) > len(self.maxheap) else float(self.maxheap[0])
    
    def addNum(self, num):
        if len(self.minheap) == len(self.maxheap):
            heapq.heappush(self.maxheap,  -heapq.heappushpop(self.minheap, -num))
        else:
            heapq.heappush(self.minheap, -heapq.heappushpop(self.maxheap, num))
        
    def findMedian(self):
        if len(self.maxheap)  == len(self.minheap):
            return (self.maxheap[0]-self.minheap[0])/2.0
        else:
            return  float(self.maxheap[0])

obj = MedianFinder()
numlist=[2,3,4]
for num in numlist:
    obj.addNum(num)
    
param_2 = obj.findMedian()
print(param_2)
