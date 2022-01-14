"""
More concise and pythonic code

Scan from the left column with a pointer at the start of each row
    try out the first k elements
    return the kth
"""

from heapq import *
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        min_heap = [(matrix[row][0], row, 0) for row in range(min(k, len(matrix)))]
        
        for i in range(k):
            answer, row, column = heappop(min_heap)
            
            if column + 1 < len(matrix[0]):
                heappush(min_heap, (matrix[row][column + 1], row, column + 1))
            
        return answer

      
      
"""
brute force: concat arrays

use min heap (put in negative of numbers)
  since we do not have a linkedlist we need to keep track of which list and what index we are currently at
similar to "merge k sorted lists" we start by adding the smallest element of each array in the heap
when we are done
  we have dealt with k elements, the arrays are sorted so we do not need to continue

return the top of the heap
"""
from heapq import *

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
