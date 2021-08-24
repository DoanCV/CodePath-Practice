"""
Two heaps
  we want to store smaller numbers in a max heap (negative of actual value) and store larger numbers in a min heap
  the top of each heap is the middle elements
    if we have even number of elements so far (the size are equal) we take the average
    if we have odd number of elements so far (size are not equal) we pop the larger heap
  to insert
    we first insert into the max heap
      keep going until the end of the list
      if the current number is greater than the top of the max heap add it
      else add it to the min heap
      we insert into the min heap if the max heap is not empty
    we want at most one element size difference between the two heaps
      so we will need to rebalance
      if the size of max heap is more than 1 element larger we pop from max heap and push negative of negative into min heap
      if the size of the max heap is smaller than the min heap we will pop from min heap and push negative into max heap
        this guaranteed our max heap is larger when the number of elements visited is odd, this doesnt matter it is just a case we have to handle, can easily be min heap        
"""
from heapq import *

class MedianOfAStream:
  min_heap = []
  max_heap = []

  def insert_num(self, num):
    
    if not self.max_heap or -self.max_heap[0] > num:  
      heappush(self.max_heap, -num)
    else:
      heappush(self.min_heap, num)

    if len(self.max_heap) > len(self.min_heap) + 1:
      heappush(self.min_heap, -heappop(self.max_heap))
    elif len(self.max_heap) < len(self.min_heap):
      heappush(self.max_heap, -heappop(self.min_heap))

  def find_median(self):
    if len(self.max_heap) == len(self.min_heap):
      return (-self.max_heap[0] + self.min_heap[0]) / 2
    return -self.max_heap[0]


def main():
  medianOfAStream = MedianOfAStream()
  medianOfAStream.insert_num(3)
  medianOfAStream.insert_num(1)
  print("The median is: " + str(medianOfAStream.find_median()))
  medianOfAStream.insert_num(5)
  print("The median is: " + str(medianOfAStream.find_median()))
  medianOfAStream.insert_num(4)
  print("The median is: " + str(medianOfAStream.find_median()))


main()

# O(logN) time complexity for insert_num where N is the size of the heaps or the numbers that are in ourr data stream. Inserting into a heap takes logN time to rebalance. O(1) time complexity for find_median since we just peak at the top of the heap which is constant time.
# O(N) space complexity since our heaps combined grow linnearly with the amount of numbers in our data stream.
