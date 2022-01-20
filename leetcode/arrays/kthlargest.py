'''
215. Kth Largest Element in an Array
Medium

Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5

Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
'''
'''
Approach 2: Quickselect

This textbook algorthm has O(N)\mathcal{O}(N)O(N) average time complexity. Like quicksort, it was developed by Tony Hoare, and is also known as Hoare's selection algorithm.

The approach is basically the same as for quicksort. For simplicity let's notice that kth largest element is the same as N - kth smallest element, hence one could implement kth smallest algorithm for this problem.

First one chooses a pivot, and defines its position in a sorted array in a linear time. This could be done with the help of partition algorithm.

    To implement partition one moves along an array, compares each element with a pivot, and moves all elements smaller than pivot to the left of the pivot.

As an output we have an array where pivot is on its perfect position in the ascending sorted array, all elements on the left of the pivot are smaller than pivot, and all elements on the right of the pivot are larger or equal to pivot.

Hence the array is now split into two parts. If that would be a quicksort algorithm, one would proceed recursively to use quicksort for the both parts that would result in O(Nlog⁡N)\mathcal{O}(N \log N)O(NlogN) time complexity. Here there is no need to deal with both parts since now one knows in which part to search for N - kth smallest element, and that reduces average time complexity to O(N)\mathcal{O}(N)O(N).

Finally the overall algorithm is quite straightforward :

    Choose a random pivot.

    Use a partition algorithm to place the pivot into its perfect position pos in the sorted array, move smaller elements to the left of pivot, and larger or equal ones - to the right.

    Compare pos and N - k to choose the side of array to proceed recursively.

    ! Please notice that this algorithm works well even for arrays with duplicates.

quickselect

'''
import random
import heapq
def findKthLargest_sort(nums, k):
    return sorted(nums)[-k]
    return heapq.nlargest(k, nums)[-1]

def findKthLargest(nums, k):
    def partition(left, right, pivot):
        p = nums[pivot]
        # move pivot to end
        nums[pivot], nums[right] = nums[right], nums[pivot]
        # move all smaller to left
        store = left
        for i in range(left, right):
            if nums[i] < p:
                nums[store], nums[i] = nums[i], nums[store]
                store+=1
        # move pivot to its final place
        nums[right], nums[store] = nums[store] , nums[right]
        return  store

    def select(left, right, k_smallest):
        if left == right:
            return nums[left]
        # select random pivot
        pivot = random.randint(left, right)
        # find pivot position in sorted list
        pivot = partition(left, right, pivot)
        # pivot is in final position
        if k_smallest == pivot:
            return nums[k_smallest]
        elif k_smallest < pivot:
            return select(left, pivot-1, k_smallest)
        else:
            return select(pivot+1, right, k_smallest)

    # kth largest is (n-k)th smallest
    return select(0, len(nums)-1, len(nums)-k)
nums = [3,2,1,5,6,4]
k = 2
print(findKthLargest(nums,k))