"""
Every number appears twice except for one, find it

Let's say we have an array - [2,1,4,5,2,4,1].
we can use xor to group the duplicates which, in pairs, evaluate to 0 and then 0 xor the single element is the single element

=> 0 ^ 2 ^ 1 ^ 4 ^ 5 ^ 2 ^ 4 ^ 1

=> 0^ 2^2 ^ 1^1 ^ 4^4 ^5 (Rearranging, taking same numbers together)

=> 0 ^ 0 ^ 0 ^ 0 ^ 5

=> 0 ^ 5

=> 5


"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        result = 0
        
        for i in range(len(nums)):
            
            result ^= nums[i]
            
        return result
