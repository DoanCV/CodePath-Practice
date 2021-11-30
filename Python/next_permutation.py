"""
if a list of numbers is in descending order, then there is no lexicographically next greater permutation
    that is why we go backwards and we search for the first occurrence of i such that nums[i] < nums[i+1]
Next, we need to search for the smallest number in nums[i:] that's larger than nums[i-1], and swap it with nums[i-1]

nums = [2,3,1,5,4,2]

i = 5
i = 4


i = 3
nums[i] > nums[i-1]
5 > 1
    j = 3
        5 > 1
    j = 4
        4 > 1
    j = 5
        2 > 1

    swap 1 and 2
    then sort everything after the 1
    
nums = [2,3,2,1,4,5]
"""
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                
                j = i
                while j < len(nums) and nums[j] > nums[i - 1]:
                    next_greater_index = j
                    j += 1
                
                nums[next_greater_index], nums[i - 1] = nums[i - 1], nums[next_greater_index]
                
                # we need to sort in place so the line below is not allowed
                # nums[i:] = sorted(nums[i:])
                # we do know one thing everything is decreasing so two pointers
                for k in range((len(nums) - i) // 2):
                    nums[i+k], nums[len(nums)-1-k] = nums[len(nums)-1-k], nums[i+k]
                
                return
        nums.reverse()
