"""
U
We are given a sorted array but it has been rotated, we do not know how many times it has been rotated
    find the minimum value

M
binary search

P
find the value in the middle
    if it is greater than the value at the right then we know that the minimum is to the right so we update our left pointer
    otherwise it is on the left or we are on it so move our right pointer
    
    when the two pointers meet we are done

E
O(logN) time complexity, where N is the length of the given array, since we are using binary search.
"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        
        while left < right:
            
            mid = (left + right) // 2
            
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
            
        return nums[left]
