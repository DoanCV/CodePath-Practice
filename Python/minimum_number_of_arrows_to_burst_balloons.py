"""
U
we have the x positions of balloons and how long they stretch across the x axis
    we can shoot arrows vertically and they can burst all balloons in the way
    since we can shoot vertically we do not care about the y position 
    we have unlimited arrows
    [1,2] and [2,3] are overlapping since the ends meet

find the minimum number of arrows we need to shoot to burst all balloons 

M
merge intervals

P
sort on end time to make it easy to find overlap

if there is no overlap then we know that we need an arrow to get that balloon
    otherwise an arrow already has the overlap covered


we sort on end time

[1,5] [3,7] [6,9] [8,10] # sorted on start time and end time

the answer is 2 but there is overlap so we would claim that 3 arrow is enough in traditional start time sort
    the difference with keeping to end time is that we can save the end of the last balloon popped going from left to right and update when there is no overlap
        if we focus on start time we will get over count

"""

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 0:
            return 0
        
        points.sort(key = lambda x: x[1])
        
        count = 1
        curr = points[0]
        for i in range(1, len(points)):
            if curr[1] < points[i][0]: # if there is no overlap we know there is another arrow necessary
                curr = points[i]
                count += 1
                
        return count
