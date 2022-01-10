"""
U
given an array of intervals with a [start, end]
    return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping 

M
merge intervals

P
sort on the interval start values
if two intervals overlap, the interval with larger end time will be removed so as to have as little impact on subsequent intervals as possible.
"""

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        if not intervals:
            return 0
        
        intervals.sort(key = lambda x: x[0])                    # sort on start time
        
        count = 0
        curr_end = intervals[0][1]
        for i in range(1, len(intervals)):
            
            if intervals[i][0] < curr_end:                      # find overlaping interval
                curr_end = min(curr_end, intervals[i][1])       # erase interval with larger end time
                count += 1
            
            else:
                curr_end = intervals[i][1]
        
        return count
