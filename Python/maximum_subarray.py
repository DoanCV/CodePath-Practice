class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Brute force:
        check every subarray
        
        Kadane's algorithm:
        keep track of the local maximum subarray
        loop through the length of the array
            you now have either the previous local max or just the current value
            update local max with the greater of the two
            
            update the global if the local is greater
        return the maximum
        
        
        ex. input =  [5,4,-1,7,8]
        [5]                     local = [5], global = [5]
        [5,4] or [4]            local = [5,4], global = [5,4]
        [5,4,-1] or [-1]        local = [5,4,-1], global = [5,4]
        [5,4,-1,7] or [7]       local = [5,4,-1,7], global = [5,4,-1,7]
        [5,4,-1,7,8] or [8]     local = [5,4,-1,7,8], global = [5,4,-1,7,8]
        
        output = 23
        """
        
        maximum_sum = nums[0]
        local_max = nums[0]
        
        for i in range(1, len(nums)):
            local_max += nums[i]
            
            local_max = max(nums[i], local_max)
            
            if local_max > maximum_sum:
                maximum_sum = local_max
        
        return maximum_sum
      
# O(N) time complexity, where N is the length of the given array, since we traverse through the array once.
# O(1) space complexity since we are not using any extra data structures.


      
