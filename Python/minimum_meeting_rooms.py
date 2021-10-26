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
    
    KEEP IN MIND THAT THE INDEXING IS SEPERATE FROM THE CLASS DEFINITION SINCE I AM CONSIDERING THE LIST OF LISTS INPUT FORMAT
    """
    def minMeetingRooms(self, intervals):
        
        min_heap = []
        
        intervals.sort(key = lambda x: x[0])
        
        heappush(min_heap, intervals[0][1])

        for meeting in range(1, len(intervals)):

            if intervals[i][0] <= min_heap[0]:
                heappop(min_heap)

            heappush(min_heap, intervals[i][0])

        return len(min_heap)


    
### Grokking solution
from heapq import *

class Meeting:
  def __init__(self, start, end):
    self.start = start
    self.end = end

  # we need to override the less than operator to use our heap
  def __lt__(self, other):
    return self.end < other.end

"""
We can't simply check for overlap then count them and add 1. 
  This is because we may have meeting that did conflict but have already ended by the time we got to a later interval.
  We would end up having more rooms than we need and the problem is asking for us to find the minimum number of required rooms.

sort the intervals by the start time
We can use a min heap to store the appointments until a meeting has ended
  while keeping track of the size of the heap
    the size of the heap is the number of rooms we will need
    we will take the largest size as our answer
  if a meeting has ended then we will remove appointments based on the end time of the top of the heap against the start time of the current meeting
"""

def min_meeting_rooms(meetings):

  meetings.sort(key = lambda x: x.start)

  min_heap = []
  min_rooms = 0

  for meeting in meetings:
    # earliest active meeting has ended we can use that room now so lets get rid of it from our heap
    while (len(min_heap) > 0 and meeting.start >= min_heap[0].end):
      heappop(min_heap)

    heappush(min_heap, meeting)

    min_rooms = max(min_rooms, len(min_heap))

  return min_rooms

def main():
  print("Minimum meeting rooms required: " + str(min_meeting_rooms(
    [Meeting(4, 5), Meeting(2, 3), Meeting(2, 4), Meeting(3, 5)])))
  print("Minimum meeting rooms required: " +
        str(min_meeting_rooms([Meeting(1, 4), Meeting(2, 5), Meeting(7, 9)])))
  print("Minimum meeting rooms required: " +
        str(min_meeting_rooms([Meeting(6, 7), Meeting(2, 4), Meeting(8, 12)])))
  print("Minimum meeting rooms required: " +
        str(min_meeting_rooms([Meeting(1, 4), Meeting(2, 3), Meeting(3, 6)])))
  print("Minimum meeting rooms required: " + str(min_meeting_rooms(
    [Meeting(4, 5), Meeting(2, 3), Meeting(2, 4), Meeting(3, 5)])))


main()

# O(N * logN) time complexity, where N is the number of intervals/meetings, since we sort on the start time
# O(N) space complexity since in the worst case our heap will have all of the meetings since they all overlap with each other.
