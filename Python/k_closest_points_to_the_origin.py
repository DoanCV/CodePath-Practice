from heapq import *
class Point:

  def __init__(self, x, y):
    self.x = x
    self.y = y

  def distance_from_origin(self):
    # we dont sqrt to calculate if one is larger
    return (self.x * self.x) + (self.y * self.y)

  # must overload the less than operator with a magic method
  def __lt__(self, other):
    return self.distance_from_origin() > other.distance_from_origin()

"""
distance formula on each point, store in a heap
  we really dont need sqrt since no matter what a value will be larger or smaller just as its sqrt

use a max heap
  store points according to their distance
  we will have a size k heap
  the largest distance will be popped and a smaller value will replace it when applicable
"""
def find_closest_points(points, k):
  result = []

  for i in range(k):
    heappush(result, points[i])
  
  for i in range(k, len(points)):
    if points[i].distance_from_origin() < result[0].distance_from_origin():
      heappop(result)
      heappush(result, points[i])

  return list(result)

# O(N * logk) time complexity, where N is the length of the given array and k is the number of points we are looking for, since we traverse through the array once and it takes O(logk) to rebalance a heap of size k.
# O(k) space complexity since we only have k elements in our heap.
