"""
Binary search on the divisors, the range of the divisors is from 1 to the max value of nums

O(NlogM) time complexity where N is the length of the given array and M is the maximum value in the array nums
O(1) space complexity since we do not use any extra data structures.
"""

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        left = 1
        right = max(nums)
        while left < right:
            mid = left + (right - left) // 2
            total = sum((num - 1) // mid + 1 for num in nums)
            
            if total > threshold:
                left = mid + 1
                
            else:
                right = mid
            
        return left
        
