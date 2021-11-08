"""
We can sort the given array and then sliding window which is O(NlogN) time

We can get O(N) by using a hashmap, {number: frequency}
    of course all numbers of the same value will be in their longest subsequence
    we can sum the frequencies and store the maximum result

"""
from collections import Counter
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        
        freq_map = Counter(nums)
        max_len = 0
        
        for i in range(len(nums)):
            
            if nums[i] - 1 in freq_map:
                max_len = max(max_len, freq_map[nums[i]] + freq_map[nums[i] - 1])
            
            # honestly we can stick to just one check, we do not need both +1 and -1 they will all get covered eventually, this will speed things up
            # if nums[i] + 1 in freq_map:
            #    max_len = max(max_len, freq_map[nums[i]] + freq_map[nums[i] + 1])
        
        return max_len
