import heapq
def square(n, i, j):
    mid = (i+j)/2
    mul = mid*mid
    if ((mul==n) or (abs(mul-n)<0.00001)):
       return mid
    elif mul<n:
        return square(n, mid, j)
    else:
        return square(n, i,  mid)

def squareroot(n):
    ans = 0
    i = 1
    found = False
    while found == False:
        if i*i == n:
            ans = i
            found = True
        elif i*i > n:
            res = square(n, i-1, i)
            ans = "{0:.5f}".format(res)
            found = True
        i+=1
    return ans

def kClosest_not_accurate(points, K) :
    res = []
    resdict = {}
    for point in points:
        euclid = (point[0])**2 + (point[1])**2
        ans = squareroot(euclid)
        resdict[ans] = point
    resdict = sorted(resdict.items())
    print(resdict)
    for i in range(K):
        res.append(resdict[i][1])
    return res

def kClosest(points, K):
    points.sort(key = lambda P : P[0]**2+P[1]**2)
    return points[:K]

def kClosest_heap(points, K):
    heap = []
    for (x,y) in points:
        dist = -(x*x+y*y)
        if len(heap) == K:
            heapq.heappushpop(heap, (dist,x,y))
        else:
            heapq.heappush(heap,(dist, x,y))
    return [[x,y] for (dist,x,y) in heap]


points = [[3,3],[5,-1],[-2,4]]
k = 2
print(kClosest(points, k))
print(kClosest_heap(points, k))