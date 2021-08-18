from heapq import *

def minimum_cost_to_connect_ropes(ropeLengths):
  """
  We will use a min heap to add the shorter ropes together first
    first store all the lengths in the heap
    then we pop two combine them and add it back to the heap
    keep track of the costs so far
    we will keep going until our heap size is 1 since we know at that point there is nothing left to combine
    return the total cost when we are done
  """
  result = []
  
  for rope in ropeLengths:
    heappush(result, rope)
  
  cost = 0
  while len(result) > 1:
    shortest_rope = heappop(result)
    next_short_rope = heappop(result)
    cost += shortest_rope + next_short_rope
    heappush(result, shortest_rope + next_short_rope)

  return cost

# O(NlogN) time complexity, where N is the length of our given array. We traverse through the given array once and then we pop n-1 times and rebalance our heap which takes logN. This makes O(N + (N-1) * logN) which is just O(NlogN).
# O(N) space complexity since our heap is size N.
