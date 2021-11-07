"""
Best solution

use a min_heap to keep track of the k pairs that can be formed from combining either the first k elements of nums1 with the first element of nums2 or all the elements of nums1 with the first element from nums2. Choosing either option depends on the length of nums1.
of course the first pair, the one with the first elements from each array is going to be part of our answer
    we get this pair from our heap we will see if the next pair will either be the next element from nums1 with the current element from nums2 or the current element from nums1 with the next element from nums2
    we keep doing this until we have k pairs

O(klogk) time complexity where k is the number of pairs that we need to find. We only have k elements in our heap at a time and will only try at most k pairs.
"""

from heapq import *
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        min_heap = []
        
        for i in range(min(k, len(nums1))):
            # heap stores tuple of 
                # (sum of pair, value from nums1, value from nums2, index in nums2)
            heappush(min_heap, (nums1[i] + nums2[0], nums1[i], nums2[0], 0))
            
            
        k_pairs = []
        while k > 0 and min_heap:
            _, value_nums1, value_nums2, position_in_nums2 = heappop(min_heap)
            
            k_pairs.append( [value_nums1, value_nums2] )
            
            # we can potentially have a pair that is smaller if the next value in nums2 is smaller than the next value in nums1
            if position_in_nums2 + 1 < len(nums2):
                
                new_candidate = value_nums1 + nums2[position_in_nums2 + 1]
                heappush(min_heap, (new_candidate, value_nums1, nums2[position_in_nums2 + 1], position_in_nums2 + 1))
                
            k -= 1
        
        return k_pairs
                



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

have a helper function to push to the minheap if the pointers are not out of range

add the smallest pair which is the first element of each list
keep finding pairs until we have k of them
we will keep increasing i or j while keeping the other the same
    Whenever a pair is chosen into the output result, the next pair in the row gets added to the priority queue of current options. 
    Also, if the chosen pair is the first one in its row, then the first pair in the next row is added to the queue

I
See class below

R
nums1=[1,7,11]
nums2=[2,4,6]

      2   4   6
   +------------
 1 |  3   5   7
 7 |  9  11  13
11 | 13  15  17

E
O(klogN) time complexity where N is the length of nums1 and k is the the number of pairs we are asked to return. We loop k times for k pairs but we add m pairs into the heap and rebalcning on the pair sum takes O(logN)
O(N) space complexity since that is the size of our heap.
"""
from heapq import *
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        
        min_heap = []
        results = []
        
        # helper function, commented code is the alterative if the helper function did not exist
        def push(i, j):
        
            if i < len(nums1) and j < len(nums2):
                heappush(min_heap, (nums1[i] + nums2[j], i, j) )
        
        
        # add the first element of each since that is guaranteed the smallest pair, then we build out
        # heappush(min_heap, (nums1[0] + nums2[0], 0, 0))
        push(0,0)
        
        while min_heap and len(results) < k:
            # position pointers
            _, i, j = heappop(min_heap)
            
            # add the smallest sum pair
            results.append([nums1[i], nums2[j]])
            
            # check the next column in our matrix representation or the next value in nums2
                # also check if we go out of range
            # if i < len(nums1) and j + 1 < len(nums2):
                # heappush(min_heap, (nums1[i] + nums2[j + 1], i, j + 1))
            push(i, j + 1)
            
            # check the next row in our matrix representation or the next value in nums1 since sum(i + 1, 0) > sum(i, 0) but sum(i, 1) > sum(i, 0) may be true
            if j == 0:
                # check if we go out of range
                # if i + 1 < len(nums1) and j < len(nums2):
                    # heappush(min_heap, (nums1[i + 1] + nums2[j], i + 1, j))
                push(i + 1, 0)
                
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
