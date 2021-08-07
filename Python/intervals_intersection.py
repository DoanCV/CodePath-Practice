"""
im going to assume both arrays are sorted on the start indicies and neither array is empty

keep track of the current interval in arr1 and arr2
  two pointers

while we are not at the end of the given arrays
  check if there is overlap
  we need to see if a start index is inside of the other interval

  if there is overlap then we need to get the exact overlap 
    maximum start and minimum end as our interval
    we append it to our results

  increment the pointers
    we need to increment the pointer with the interval that ends earlier since the next one may have overlap with the other interval that the other pointer is at
  
return results
"""

def merge(intervals_a, intervals_b):
  result = []
  curr_arr1 = 0
  curr_arr2 = 0

  while curr_arr1 < len(intervals_a) and curr_arr2 < len(intervals_b):
    a_start_in_b = intervals_a[curr_arr1][0] <= intervals_b[curr_arr2][1] and intervals_a[curr_arr1][0] >= intervals_b[curr_arr2][0]
    b_start_in_a = intervals_b[curr_arr2][0] <= intervals_a[curr_arr1][1] and intervals_b[curr_arr2][0] >= intervals_a[curr_arr1][0]
    
    if (a_start_in_b or b_start_in_a):
      start = max(intervals_a[curr_arr1][0], intervals_b[curr_arr2][0])
      end = min(intervals_a[curr_arr1][1], intervals_b[curr_arr2][1])
      result.append([start, end])

    if intervals_a[curr_arr1][1] < intervals_b[curr_arr2][1]:
      curr_arr1 += 1
    else:
      curr_arr2 += 1

  return result


def main():
  print("Intervals Intersection: " + str(merge([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]])))
  print("Intervals Intersection: " + str(merge([[1, 3], [5, 7], [9, 12]], [[5, 10]])))


main()

# O(N + M) time complexity, where N is the length of intervals_a and M is the length of intervals_b, since in the worst case we have to reach the end of both arrays. Regardless, we have to reach the end of one of the arrays.
# O(1) space complexity if we ignore the output array.
