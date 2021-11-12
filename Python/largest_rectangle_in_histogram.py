"""
Before adding a new building, pop the buildings taller than the new one. The building popped out represent the height of a rectangle with the new building as the right boundary and the current stack top as the left boundary

[2,1,5,6,2,3] -> [2,1,5,6,2,3,0]

stack = [-1]
max = 0

bar index = 0
stack = [-1, 0]
max = 0

bar index = 1
stack = [-1, 1]
max = 2

bar index = 2
stack = [-1, 1, 2]
max = 2

bar index = 3
stack = [-1, 1, 2, 3]
max = 2

    heights[4] = 2 < 6
    max = 6
    stack = [-1, 1, 2]
    heights[4] = 2 < 5
    max = 10
    stack = [-1, 1]

bar index = 4
stack = [-1, 1, 4]
max = 10

bar index = 5
stack = [-1, 1, 4, 5]
max = 10

bar index = 6
stack = [-1, 6]
max = 10
"""
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        max_size = 0
        
        stack = []
        stack.append(-1) # this way we will never get empty stack and we know that -1 index is the last bar so we make that 0
        
        # we need to add an extra element, a 0 like in the histogram problem
        # in the case where the given heights are all in ascending order, it creates an ending point that breaks this trend, allowing us to calculate the areas
        heights.append(0)

        for bar in range(len(heights)):

            # if we find height[i]'s >= what we currently see in the stack we add to the stack
            # this way our stack elements are always in ascending order
            while heights[bar] < heights[stack[-1]]:
                
                full_bar_height = heights[stack.pop()]
                
                width = bar - stack[-1] - 1 # avoid double count of left and right boundaries
                
                max_size = max(max_size, full_bar_height * width)

            stack.append(bar)
            
        return max_size 


    
    
    
    
# almost the same just not written as well as the above    
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
