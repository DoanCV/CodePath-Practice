"""
Given the availability time slots arrays slots1 and slots2 of two people and a meeting duration duration, return the earliest time slot that works for both of them and is of duration "duration".

If there is no common time slot that satisfies the requirements, return an empty array.

The format of a time slot is an array of two elements [start, end] representing an inclusive time range from start to end.  

It is guaranteed that no two availability slots of the same person intersect with each other. That is, for any two time slots [start1, end1] and [start2, end2] of the same person, either start1 > end2 or start2 > end1.

 
Example 1:
Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 8
Output: [60,68]


Example 2:
Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 12
Output: []




We can use two heaps, one for each list of slots or we can just sort on the start time and use two pointers
"""

def meeting_scheduler(slots1, slots2, duration):

  # sort on the start times
  slots1.sort(key = lambda x: x[0])
  slots2.sort(key = lambda x: x[0])

  i1 = 0
  i2 = 0
  while i1 < len(slots1) and i2 < len(slots2):

    # check if there is an intersect for long enough
    start = max(slots1[i1][0], slots2[i2][0]) # later start time
    end = min(slots1[i1][1], slots2[i2][1]) # earlier end time

    if end - start >= duration:
      return [start, start + duration] # we want the earliest start time possible
    
    # no intersect
    if slots2[i2][0] > slots1[i1][0]:
      i1 += 1
    else:
      i2 += 1

  # no such interval exists
  return []

meeting_scheduler([[10,50],[60,120],[140,210]], [[0,15],[60,70]], 12)
meeting_scheduler([[10,50],[60,120],[140,210]], [[0,15],[60,70]], 8)
