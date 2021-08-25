from heapq import *
import heapq

class SlidingWindowMedian:
  """
  Two heaps (one min heap, one max heap)
  just like median in data stream
    we will store the smaller numbers in the min heap
    we will store the larger numbers in the max heap
  however this time, the size of the heaps together is at most k
    also, we do not calculate the median until we hit the size k
  """

  def __init__(self):
    self.min_heap = []
    self.max_heap = []

  def find_sliding_window_median(self, nums, k):
    # intialize an array of floats where we will store the median
      # it will be k less than the size of nums
    result = [0.0 for i in range(len(nums) - k + 1)]

    # loop through nums
    for window_end in range(len(nums)):
      # add element
      # if the max_heap is not empty or if the current element is less than the top of the max_heap, add to max_heap
      if not self.max_heap or nums[window_end] <= -self.max_heap[0]:
        heappush(self.max_heap, -nums[window_end])
      # else add to min_heap
      else:
        heappush(self.min_heap, nums[window_end])

      # rebalance heaps
      self.rebalance()

      window_start = window_end - k + 1

      # calculate the median if we have k elements in our sliding window
      if window_start >= 0:
        
        # if we have the same size for both heaps just append the average of the top of each heap to results
          # otherwise peak from the max_heap since that is the median
        if len(self.min_heap) == len(self.max_heap):
          result[window_start] = (self.min_heap[0] + -self.max_heap[0]) / 2 
        else:
          result[window_start] = self.max_heap[0]

        # remove element from sliding window
          # the start of our sliding window is the element we want to remove
        # we need to figure out which heap it is from
        remove_this = nums[window_start]
        if remove_this <= -self.max_heap[0]:
          self.remove_element(self.max_heap, -remove_this)
        else:
          self.remove_element(self.min_heap, remove_this)

        # rebalance heaps since we removed an element
        self.rebalance()

    # return array of medians
    return result
  
  def rebalance(self):
    # we will have the two heaps either be the same size or in the case of odd length nums, my preference is to have a larger max_heap
    # two cases
      # max_heap is larger than min_heap by more than 1
      if len(self.max_heap) > len(self.min_heap) + 1:
        heappush(self.min_heap, -heappop(self.max_heap))
      # max_heap is smaller than min_heap
      elif len(self.max_heap) < len(self.min_heap):
        heappush(self.max_heap, -heappop(self.min_heap))

  def remove_element(self, heap, remove_this):
    # given the element we want to remove, find it and remove it
    index = heap.index(remove_this)

    # set the element to the end value
    # remove the end value
    heap[index] = heap[-1]
    del heap[-1]

    # percolate up
    if index < len(heap):
      heapq._siftup(heap, index) # percolate up
      heapq._siftdown(heap, 0, index) # percolate down (heap, start position, position)
    


def main():

  slidingWindowMedian = SlidingWindowMedian()
  result = slidingWindowMedian.find_sliding_window_median(
    [1, 2, -1, 3, 5], 2)
  print("Sliding window medians are: " + str(result))

  slidingWindowMedian = SlidingWindowMedian()
  result = slidingWindowMedian.find_sliding_window_median(
    [1, 2, -1, 3, 5], 3)
  print("Sliding window medians are: " + str(result))


main()

