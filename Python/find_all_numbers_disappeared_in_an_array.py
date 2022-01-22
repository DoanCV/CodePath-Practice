"""
We are given an array of n integers in the range 1 to n
    return an array of all integers in the range 1 to n that do no appear in the given array

Few ideas
    worst one is to search the rest of the array for each value in the solution space from 1 to n
    slightly better is to sort and scan with binary search
    slightly better in time complexity is to create a boolean array to mark down what has been found

Better ideas that are time and space optimized
    cyclic sort, i will implement this one
    using the given array as the "boolean array" since 1 to n is positive, negative values will denote what we have seen

"""

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        for i in range(len(nums)):
            while nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
                
        return [i for i in range(1, len(nums) + 1) if nums[i - 1] != i]
