'''
Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
'''

def intervalIntersection(A,B):
    ans = []
    i = 0
    j = 0
    while i < len(A) and j<len(B):
        low = max(A[i][0], B[j][0])
        high = max(A[j][1], B[j][1])
        if low<=high:
            ans.append([low, high])
        if A[i][1] < B[j][1]:
            i+=1
        else:
            j+=1
            
    return ans
A = [[0,2],[5,10],[13,23],[24,25]]
B = [[1,5],[8,12],[15,24],[25,26]]
print(intervalIntersection(A,B))

