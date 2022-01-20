"""
U
we have n online courses, numbered 1 to n
we are given an array called courses, wehre courses[i] = [duration, lastDay]
    this means that the ith course should be taken continuously for duration and must be finished by last day 
    
find the maximum number of course that you can take

M
greedy with a max heap

P
sort the courses on the last day
for all the courses we choose to take the sum of the duration
    remove the largest-length course from the sum of the duration until the total duration has less than end
    
this will leave us with the maximum numebr of courses
"""

from heapq import *

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        
        max_heap = []
        
        time = 0
        
        for duration, last_day in sorted(courses, key = lambda x: x[1]):
            time += duration
            
            heappush(max_heap, -duration)
            
            while time > last_day:
                time += heappop(max_heap)
                
        return len(max_heap)
