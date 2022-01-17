"""
lets try quickselect instead since that way we can get average case linear time
    heap approach, which similar to sorting, makes the problem trivial
    
    
find pivot point to split the array into three groups
    elements smaller than pivot, elements equal to pivot, elements greater than pivot
determine how many elements are in each group

note: since we are looking for kth largest, lets say left is larger than k and right is less than k

if k <= left 
    we know to look left
if k > left + mid
    look at right part
else
    we are in the middle part and we are done
"""
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        if not nums:
            return
        
        pivot = random.choice(nums)
        
        greaterThanPivot = [x for x in nums if x > pivot]
        mid = [x for x in nums if x == pivot]
        lessThanPivot = [x for x in nums if x < pivot]
        
        L = len(greaterThanPivot)
        M = len(mid)
        
        if k <= L:
            return self.findKthLargest(greaterThanPivot, k)
        elif k > L + M:
            return self.findKthLargest(lessThanPivot, k - L - M)
        else:
            return mid[0]

        
        
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
