from heapq import *

"""
brute force: concat arrays

use min heap (put in negative of numbers)
  since we do not have a linkedlist we need to keep track of which list and what index we are currently at
similar to "merge k sorted lists" we start by adding the smallest element of each array in the heap
when we are done
  we have dealt with k elements, the arrays are sorted so we do not need to continue

return the top of the heap
"""

def find_Kth_smallest(lists, k):
  min_heap = []

  # put first element of each list into the heap
  for i in range(len(lists)):
    heappush( min_heap, (lists[i][0], i, 0) )

  visited = 0
  while min_heap:
    number, curr_list_position, position_in_list = heappop(min_heap)

    visited += 1
    if visited == k:
      break

    if position_in_list + 1 < len(lists[curr_list_position]):
      heappush(min_heap, (lists[curr_list_position][position_in_list + 1], curr_list_position, position_in_list + 1))
      
  return number

# O(k * logM) time complexity, where M is the number of lists and k is given. We limit our heap to size M so rebalancing is logk. We only visit k elements since at that point we are done. We start from the smallest elements and keep going until the kth smallest element.
# O(M) space complexity since M is the size of our heap.
