from math import ceil
# O(nm)-time, O(1)-space
def minEatingSpeed_bruteforce(piles, h):
    speed = 1
    while True:
        hours_spent = 0
        for pile in piles:
            hours_spent += ceil(pile/speed)
        if hours_spent <= h:
            return speed
        else:
            speed+=1

def minEatingSpeed_binarysearch(piles,h) :
    left = 1
    right = max(piles)
    while left<right:
        middle = (left+right)//2
        hours_spent = 0
        for pile in piles:
            hours_spent += ceil(pile/middle)
        if hours_spent <=h:
            right = middle
        else:
            left = middle+1
    return right
piles = [3,6,7,11]
h = 8
print(minEatingSpeed_binarysearch(piles,h))
print(minEatingSpeed_bruteforce(piles, h))