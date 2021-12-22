"""
We have n lines that are bounds for containers
    water cant be stored above the maximum height line
    we want the maximum area since that container hold the most water


To calculate the area we need the width and the height
We have to scan through the entire array since even though the start and end may be the answer
    consider cases where the heights are very high


Two pointers
    one at the start (left) and one at the end (right)
    
    take the lower of the heights and calculate the area and update max area
    
    move left pointer if the left height is smaller
        otherwise move the right pointer back
    
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            
            max_area = max(max_area, min(height[left], height[right]) * (right - left))
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area
