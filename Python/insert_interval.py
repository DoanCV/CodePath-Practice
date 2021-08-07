"""
### One way is to insert the new interval, sort on the start, then merge with the algorithm from merge intervals but we can beat sorting's O(NlogN)

keep track of the current interval

while the new_interval does not overlap and we are not at the end of the intervals (if the new interval start is greater than the end of an interval)
  Skip intervals 
  when we skip we just dont merge but we still append it to an output

# otherwise we need to merge the overlap
while not at the end and we are not at the end of the intervals (new end is greater than current start)
  get the start and end of the merged interval by comparing the lower start and higher end

append the merged interval to the output

# get the remaining intervals
while not at the end
  append the rest

return output array
"""

def insert(intervals, new_interval):
  merged = []
  
  i = 0
  while i < len(intervals) and new_interval[0] > intervals[i][1]:
    merged.append(intervals[i])
    i += 1
  
  while i < len(intervals) and new_interval[1] >= intervals[i][0]: 
    new_interval[0] = min(new_interval[0], intervals[i][0])
    new_interval[1] = max(new_interval[1], intervals[i][1]) 
    i += 1
  
  merged.append(new_interval)

  while i < len(intervals):
    merged.append(intervals[i])
    i += 1

  return merged


def main():
  print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 6])))
  print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 10])))
  print("Intervals after inserting the new interval: " + str(insert([[2, 3], [5, 7]], [1, 4])))


main()


# O(N) time complexity, where N is the length of the given list of intervals, since we traverse through the list of itnervals once.
# O(N) space complexity since we have an output array which contains the merged itnervals. In the worst case no intervals are merged and the array reaches size N + 1 which is just N.
