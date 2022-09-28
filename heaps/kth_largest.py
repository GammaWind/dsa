'''
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

You must solve it in O(n) time complexity.

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

'''

#We are solving this using heap where the complexity would be O(n * klogk)
#sc = O(k)


from heapq import heapify
import heapq
from typing import List
nums = [3,2,1,5,6,4]
k = 4

def get_kth_largest(arr: List[int], k: int ) -> int:
    
    #define a minheap of size k
    heap_lst = []
    # for i in range(0,k):
    #     heap_lst.append(arr[i])
    heapq.heapify(heap_lst)

    for i in range(0, len(arr)):
        heapq.heappush(heap_lst, arr[i])
        if len(heap_lst) > k:
            heapq.heappop(heap_lst)

    return heap_lst[0]

ans= get_kth_largest(nums, k)
print(ans)            

