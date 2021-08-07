class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Division is allowed: 
        find the product of the whole array with one loop, then loop again but divide out the current value and append result to output array
        
        
        No division:
        
        the product of array except self is a product of left and right elements apart from self
        
        loop through the array from left to right and get a product of everything to the left so far (do not include current)
        
        loop through the array from right to left and get a product of everything to the right so far (do not include current)
        
        for each index in both arrays, find the product and append to the output array
        
        
        ex. nums = [1,2,3,4]
        the left of nums[0] is 1 and the right of nums[len(nums) - 1] is 1
        left: [1, 1, 2, 6]
        right: [24,12, 4, 1]
        
        output: [24,12,8,6]
        
        """
        
        left = [1] * (len(nums))
        prod = left[0]
        for i in range(1, len(nums)):
            prod = prod * nums[i - 1]
            left[i] = prod
        
        right = [1] * (len(nums))
        prod = right[len(nums) - 1]
        for i in range(len(nums) - 2, -1, -1):
            prod = prod * nums[i + 1]
            right[i] = prod
        
        output = [1] * (len(nums))
        for i in range(len(nums)):
            output[i] = left[i] * right[i]
        
        return output
      
      
# O(N) time complexity, where N is the length of the given array, since we are traversing through the array three times independently. 3N reduces to N.
# O(N) space compelexity since we are creating three arrays that are the same size as the given array. We keep track of the left products, right products and the output array.
