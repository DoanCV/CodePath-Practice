class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        """
        two pointers to find a subarray where the order changes, left pointer starts at the beginning and right starts at the end
        move one at a time move low to first out of order
        find the min and max of the array 
        extend subarray until it has that min and max
        """
        
        low = 0
        high = len(nums) - 1
        
        # move start pointer
        while low < len(nums) - 1 and nums[low] <= nums[low + 1]:
            low += 1
        
        # if the array is already sorted
        if len(nums) - 1 == low:
            return 0
        
        #  move end pointer
        while high > 0 and nums[high] >= nums[high - 1]:
            high -= 1
        
        # find the max/min
        minimum = 1000000
        maximum = -1000000
        
        
        for i in range(low, high + 1):
            minimum = min(minimum, nums[i])
            maximum = max(maximum, nums[i])
        
        # extend
        while low > 0 and nums[low - 1] > minimum:
            low -= 1
        
        while high < len(nums) - 1 and nums[high + 1] < maximum:
            high += 1
        
        return high - low + 1
      
# O(N) time complexity, where N is the length of the given array, since we traverse the given array linearly with sinlge loops.
# O(1) space complexity since we are not using any other data structures.
