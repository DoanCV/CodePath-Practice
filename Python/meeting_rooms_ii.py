"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

"""
Greedy Solution

sort the intervals on the start time
add the first element to the min heap
loop through the remainder of the meetings
if we have a meeting start time that is greater than or equal to the top of our heap then we know we can reuse that room for the current meeting
"""

from heapq import *
class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def minMeetingRooms(self, intervals):
        
        min_heap = []
        
        intervals.sort(key = lambda x: x[0])
        
        heappush(min_heap, intervals[0][1])

        for meeting in range(1, len(intervals)):

            if intervals[i][0] >= min_heap[0]:
                heappop(min_heap)

            heappush(min_heap, intervals[i][1])

        return len(min_heap)


