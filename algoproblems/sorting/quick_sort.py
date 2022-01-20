import unittest

def quickSort(array):
    start = 0
    end = len(array)-1
    quickSort_helper(array, start, end)
    return array

def quickSort_helper(array, left, right):
    if left >=right:
        return
    p = left
    l = left+1
    r = right
    while l<=r:
        if array[l] > array[p] and array[r] < array[p]:
            swap(array, l, r)
        if array[l] <= array[p]:
            l+=1
        if array[r] >= array[p]:
            r-=1
    swap(array, p, r)
    leftsubarraysmaller = r-1-left < right-(r+1)
    if leftsubarraysmaller:
        quickSort_helper(array, left, r-1)
        quickSort_helper(array, r+1, right)
    else:
        quickSort_helper(array, r+1, right)
        quickSort_helper(array, left, r-1)
def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(quickSort([8, 5, 2, 9, 5, 6, 3]), [2, 3, 5, 5, 6, 8, 9])