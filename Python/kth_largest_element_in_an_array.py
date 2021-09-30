"""
U
We have an array of integers and an integer k

find the kth largest element in the array

the given test cases are enough

M
We can either sort and return the kth value from the end

However we can beat this with a max heap
    we can insert and then at the end pop k times and return the kth element
    or we can have min heap of size k and then return the top when we are done

P
I will use a min_heap

IRE

"""
from heapq import * 
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        min_heap = []
        
        for i in range(len(nums)):
            
            heappush(min_heap, nums[i])
            
            if len(min_heap) > k:
                heappop(min_heap)
                
        
        return heappop(min_heap)
