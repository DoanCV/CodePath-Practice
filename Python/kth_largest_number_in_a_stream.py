from heapq import *

class KthLargestNumberInStream:
  # use min_heap since we keep the smallest at the top and when we limit the size to k the top will always be the kth largest
  min_heap = []

  def __init__(self, nums, k):
    # take in k
    self.k = k
    # take in stream of integers
    for num in nums:
      self.add(num)

  def add(self, num):
    # add number
    heappush(self.min_heap, num)

    # if heap size is greater than k, pop the top (lowest number) and then rebalance
    if len(self.min_heap) > self.k:
      heappop(self.min_heap)
    
    # return kth largest element    
    return self.min_heap[0]


def main():

  kthLargestNumber = KthLargestNumberInStream([3, 1, 5, 12, 2, 11], 4)
  print("4th largest number is: " + str(kthLargestNumber.add(6)))
  print("4th largest number is: " + str(kthLargestNumber.add(13)))
  print("4th largest number is: " + str(kthLargestNumber.add(4)))
  
# O(logk) time complexity for add() where k is given. It takes O(logk) time to rebalance a size k heap after popping.
# O(k) space compleixty since our heap has k elements.
