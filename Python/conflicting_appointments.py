"""
sort then check if the end is greater than the start of the next interval, equal is ok
"""
def can_attend_all_appointments(intervals):
  intervals.sort(key = lambda x: x[0])
  
  for i in range(1, len(intervals)):
    if intervals[i-1][1] > intervals[i][0]: 
      return False
  
  return True


def main():
  print("Can attend all appointments: " + str(can_attend_all_appointments([[1, 4], [2, 5], [7, 9]])))
  print("Can attend all appointments: " + str(can_attend_all_appointments([[6, 7], [2, 4], [8, 12]])))
  print("Can attend all appointments: " + str(can_attend_all_appointments([[4, 5], [2, 3], [3, 6]])))


main()

# O(N) time complexity, where N is the number of intervals in the given array, since we have to visit each interval once.
# O(1) space complexity since we are not using any extra data structues.
