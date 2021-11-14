"""
At first glance I thought sliding window but then I realized what happens when we have a smaller window that is valid but we confirmed a larger one? Our count is wrong.
    Nothing is given to us sorted so its bait. We also can have negative integers.



We will have to use prefix sum to keep track of the cumulative sum
    then we have a hashmap to keep track of the frequency in which we see a given prefix sum
    we use this frequency to get the number of subarrays
    dict = {value: frequency}
    
k = sum[end] - sum[start]
    where end is the cumulative sum and start is a cumulative sum in the hashmap
    
we check in this form: sum[end] - k == sum[start]
    we have the first two values so this works
    
ex.
[1,2,3], k = 3

i = 0
cum_sum = 1
count = 0
we will add 0 with frequency of 1
    the cumulative sum of nothing is 0
dict = {0: 1}

i = 1
cum_sum = 3
count = 1
dict = {0: 1, 1: 1, 3: 1}

i = 2
cum_sum = 6
count = 2
    because cum_sum - 3 in hashmap
dict = {0: 1, 1: 1, 3: 1, 6: 1}

"""

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        sums = {}
        sums[0] = 1
        
        curr_sum = 0
        count = 0
        
        for i in range(len(nums)):
            
            curr_sum += nums[i]
            
            if (curr_sum - k) in sums:
                count += sums[curr_sum - k]
                
            if curr_sum in sums:
                sums[curr_sum] += 1
            else:
                sums[curr_sum] = 1
        
        return count
       
# O(N) time complexity, where N is the length of the given array, since we traverse through the given array once and use constant time lookups with our hashmap.
# O(N) space complexity. Our hashmap is worst case the size of the given array + 1. The sums do not repeat unless we have a 0 in the matrix.
