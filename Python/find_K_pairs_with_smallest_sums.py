"""
U
We are given two arrays and both are already sorted

return the k smallest sum pairs

a pair is a number from nums1 and another from nums2

test cases are not enough
    numbers can be negative
    otherwise the following are covered
        no empty array
        duplicate numbers are fine

edge case
    k can be larger than the possible number of combinations
    
M
Brute force
    find all combinations and then find the k smallest after a sort

better
    we can find all combinations and put them into a heap with the priority being the sum
    we will then pop k times and add each pair to a result list an return it
    minheap since we pop k times when we added all pairs to the heap

### The above works but our heap will grow too large, see below

But we are given ascending order, can we take advantage of this?
    we can go back to this later but it seems like we do not need all of the combinations
    maybe limit the size of the heap to just k so we pop when the size is greater

### Now the above is too slow

We need to take advantage of the given sorted arrays
We can treat this similar to kth smallest element from m sorted arrays
    keep track of the samllest values in each array
        start at the beginning since both are the smallest from their respective arrays
        we will push pairs until we hit k
    it is impossible 
        for sum(i + 1, j) < sum(i, j) or 
        for sum(i, j + 1) < sum(i, j) or 
        for sum(i + 1, j + 1) < sum(i + 1, j) or 
        for sum(i + 1, j + 1) < sum(i, j + 1)  
    
P
Generate all possible pairs get thier sum and add it to the minheap

pop k times and store in a results list

return the results

### The above works but our heap will grow too large

store the negative of the given sum so that it gets removed first
    this is a max heap

### Now the above is too slow



IRE
"""
from heapq import *
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        min_heap = []
        results = []
        
        # add the first element of each since that is guaranteed the smallest pair, then we build out
        heappush(min_heap, (nums1[0] + nums2[0], 0, 0))
        
        while min_heap and len(results) < k:
            # position pointers
            _, i, j = heappop(min_heap)
            
            # add the smallest sum pair
            results.append([nums1[i], nums2[j]])
            
            # check the next column in our matrix representation or the next value in nums2
                # also check if we go out of range
            if i < len(nums1) and j + 1 < len(nums2):
                heappush(min_heap, (nums1[i] + nums2[j + 1], i, j + 1))
            
            # check the next row in our matrix representation or the next value in nums1 since sum(i + 1, 0) > sum(i, 0) but sum(i, 1) > sum(i, 0) may be true
            if j == 0:
                # check if we go out of range
                if i + 1 < len(nums1) and j < len(nums2):
                    heappush(min_heap, (nums1[i + 1] + nums2[j], i + 1, j))
        return results
"""        
from heapq import *
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
                
        min_heap = []
        
        # generate all pairs
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                pair_sum = nums1[i] + nums2[j]
                heappush(min_heap, (-pair_sum, nums1[i], nums2[j]) )
                
                if len(min_heap) > k:
                    heappop(min_heap)
        
        result = []
        
        if len(min_heap) < k:
            while min_heap:
                pair_sum, nums1_val, nums2_val = heappop(min_heap)
                result.append([nums1_val, nums2_val])
        else:
            for i in range(k):
                pair_sum, nums1_val, nums2_val = heappop(min_heap)
                result.append([nums1_val, nums2_val])
            
        return result
"""