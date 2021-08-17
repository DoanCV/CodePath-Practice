from heapq import *

def find_Kth_smallest_number(nums, k):

      """
      brute force: sort and return kth element


      max heap 

      heapq is a minheap naturally so we have high priority for smaller elements
      we want the k smallest numbers so we want to remove larger elements and push smaller elments into our size k minheap
      to get larger elements to have higher priority we negate everything
      when we are done return top element and undo the negation 
      """

      heap = []

      for i in range(k):
            heappush(heap, -nums[i])
      
      for i in range(k, len(nums)):
            if -nums[i] > heap[0]:
                  heappop(heap)
                  heappush(heap, -nums[i])
      
      return -heappop(heap)
      
# O(N * logk) time complexity, where N is the length of the given array, since we traverse through the array once without repeating any calculations and it takes O(logk) to extract and rebalance heap. 
# O(k) space complexity since k is the size of the max heap
