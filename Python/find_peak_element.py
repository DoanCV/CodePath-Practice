"""
U
given an array of integers find a peak element and return its index
    there can be multiple but return the index one of them, does not matter which one
    a peak element is an element that is greater than its immediate neighbors

M/P
we can use binary search even if the values are not sorted since the element to the left of the leftmost and the element to the right of the rightmost is -inf
    this means there is a local max
    we will look for it
    
find mid, compare with left and right neighbors
    if mid greater then neighbors return it since we can return any peak
    if mid smaller than right neighbor take the right half
    otherwise take the left
"""
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        left = 0
        right = len(nums) - 1
        
        while left < right:
            
            mid = (left + right) // 2
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid

            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid - 1
            
        return left
