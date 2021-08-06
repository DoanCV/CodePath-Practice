from __future__ import print_function


class Interval:
  def __init__(self, start, end):
    self.start = start
    self.end = end

  def print_interval(self):
    print("[" + str(self.start) + ", " + str(self.end) + "]", end='')

"""
an interval class instead of a 2D array???? bruh

# if there is only one interval return that interval

sort the intervals on the start of the intervals

keep track of the start and end of a valid interval starting with the first pair
loop through each interval
  check for overlap, if the current start is less than the end of the previous
    we have overlap so the greater end value is the end of this valid interval

  otherwise add the start and end to the results and update the start and end with the current start and end

add the last interval to the result since there is nothing left to check
return result

ex. (I represented as 2D array but that is not what is given, pretty sure no one will go through the hassle of making a class)
input: [[1,2], [3,4]]
output: [[1,2], [3,4]]

input: [[1,4], [3,6]]
output: [[1,6]]

input: [[1,2], [1,4]]
output: [[1,4]]

input: [[1,4], [1,2]]
output: [[1,4]]

input: [[6,7], [2,4], [5,9]]
output: [[2,4],[5,9]]
"""
def merge(intervals):
  if len(intervals) < 2:
    return intervals

  intervals.sort(key = lambda x: x.start)

  merged = []
  
  start = intervals[0].start
  end = intervals[0].end

  for curr in intervals:
    # overlap
    if end >= curr.start: 
      if curr.end > end:
        end = curr.end
    # no overlap
    else:
      merged.append(Interval(start,end))
      start = curr.start
      end = curr.end

  merged.append(Interval(start,end))

  return merged


def main():
  print("Merged intervals: ", end='')
  for i in merge([Interval(1, 4), Interval(2, 5), Interval(7, 9)]):
    i.print_interval()
  print()

  print("Merged intervals: ", end='')
  for i in merge([Interval(6, 7), Interval(2, 4), Interval(5, 9)]):
    i.print_interval()
  print()

  print("Merged intervals: ", end='')
  for i in merge([Interval(1, 4), Interval(2, 6), Interval(3, 5)]):
    i.print_interval()
  print()

main()


# O(NlogN) time complexity, where N is the length of the given "array", since we are sorting by the start of each interval. That is our most time consuming operation since after that we traverse through the given "list" of intervals once
# O(N) space compelexity since we are creating a new array which stores the merged intervals. In the worst case, none of the given intervals can be merged so the array is size N.
