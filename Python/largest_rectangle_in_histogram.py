class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_size = 0
        heights.append(0)
        
        for bar, height in enumerate(heights):
            while stack and heights[stack[-1]] >= height:
                
                full_bar_height = heights[stack.pop()]
                
                if not stack:
                    width = bar
                else:
                    width = bar - stack[-1] - 1
                
                max_size = max(max_size, full_bar_height * width)
            
            stack.append(bar)
            
        return max_size 

"""
we know that the largest area always has at least one complete bar
    since this is the case we can use a stack to keep track of the left and right boundaries where the bars to the left and right have a lower height
    this tells us which bars are not part of the rectangle

we do not have to use a stack
    just have two arrays, left and right
    left[i] indicates how many consecutive bars to the left including the bar at index i are at least higher than heights[i], right[i] is that to the right
    the width of each bar is 1 so we can do this
        having the number of bars is effectively the width as well

width = left + right - 1
area = height of full bar * width

O(N) time complexity where N is the length of the given array. The while loop in the for loop jumps forwards or backwards by the steps already calculated we do not repeatedly search. It jumps by the contiguous groups.
"""

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        n = len(heights)
        
        left = [1 for i in range(n)]
        right = [1 for i in range(n)]
        
        # left to right
        for i in range(n):
            
            j = i - 1
            while j >= 0 and heights[j] >= heights[i]:
                j -= left[j]
            
            left[i] = i - j # width is also number of bars
            
        # right to left    
        for i in range(n - 2, -1, -1):
            
            j = i + 1
            while j < n and heights[j] >= heights[i]:
                j += right[j]
            
            right[i] = j - i
        
        
        max_rectangle_area = 0
        for i in range(n):
            # subtract one from the sum since we do not want to double count the current bar
            max_rectangle_area = max(max_rectangle_area, (left[i] + right[i] - 1) * heights[i] ) 
            
        return max_rectangle_area
