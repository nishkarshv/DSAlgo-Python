def mergesorted_1(num1, m, num2, n):

    i=0
    j=0
    num1_copy = num1[:m]
    num1[:] = []
    while i < m and j < n:
        if num1_copy[i]<num2[j]:
            num1.append(num1_copy[i])
            i+=1
        else:
            num1.append(num2[j])
            j+=1
    if i<m:
        num1[i+j:] = num1_copy[i:]
    if j<n:
        num1[i+j:] = num2[j:]


def mergesorted(num1, m, num2, n):

    i=m-1
    j=n-1
    k = m+n-1
    while i>=0 and j>=0:
        if num1[i]<num2[j]:
            num1[k] = num2[j]
            j-=1
        else:
            num1[k] = num1[i]
            i-=1
        k-=1
    
    num1[:j+1] = num2[:j+1]
    

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
mergesorted_1(nums1, m, nums2, n)
print(nums1)