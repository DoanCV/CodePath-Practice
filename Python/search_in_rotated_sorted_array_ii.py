"""
Exactly the same as search in rotated sorted array I
    except we need to take care of duplicates
    we can just shift the left pointer up if the elements between the left and the mid point are the same
"""
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            
            mid = (right + left) // 2
            
            if nums[mid] == target:
                return True
            
            while left < mid and nums[left] == nums[mid]:
                left += 1
            
            if nums[left] <= nums[mid]:
                
                if nums[left] <= target and target < nums[mid]:
                    right = mid - 1
                
                else:
                    left = mid + 1
                    
            else:
                
                if nums[right] >= target and target > nums[mid]:
                    left = mid + 1
                    
                else:
                    right = mid - 1
        
        return False
