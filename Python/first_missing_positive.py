"""
We are given an unsorted array. Return the first missing positive integer.
    The array can have negative values
    duplicates? nope


Two cases
    1. the array is not missing a positive integer
    2. the array is missing a positive integer

The two cases limit the possible answers to 1 to n + 1 where n is the length of the given array
    in case 1, the answer will be the next value past the length of the given array so n + 1
        this is because the array is full and has all of the positive integers up to n
    in case 2, the answer must be within 1 to n

We can use extra space to which value from 1 to n is missing but since our solution space is limited to the size of our input and we do not have duplicates, we can use a trick.
  let the index of each element of the array represent the value from 1 to n, obviously we need to adjust by 1 since python is 0 indexed, if we found a number in the range then the value at the index will be negative
  this is essentially hashing the index to a "bool" telling us if the number is missing or not
  once we scan again the first positive value we find will tell us that index + 1 is our answer
  
ex. 
nums = [3,4,-1,1]

change irrelevant values to len(nums) + 1
    i.e. n + 1
nums = [3,4,5,1]

i = 0
nums = [3,4,-5,1]

i = 1
nums = [3,4,-5,-1]


O(N) time complexity where N is the length of the given array since we solve with three linear passes.
O(1) space complexity since we just modify the given array
"""
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        # change all irrelevant values so we can hash them to one index key
        for i in range(n):
            if nums[i] < 1 or nums[i] > n:
                nums[i] = n + 1
        
        for i in range(n):
            num = abs(nums[i])
            
            if num > n:
                continue
            
            num -= 1 # python indexing
            if nums[num] > 0: # prevents double negative operations
                nums[num] *= -1 
        
        # find the first cell which isn't negative
        for i in range(n):
            if nums[i] >= 0:
                return i + 1
            
        # no positive numbers were found, which means the array contains all numbers 1..n
        return n + 1
