from heapq import *

"""
Use a min heap
  we need the largest numbers and in heapq when we pop we get the smallest element since they get higher priority
  so we will insert only k elements into the heap
  if the current value is greater than what is in the heap, we remove the smallest element and push the current value
"""

def find_k_largest_numbers(nums, k):
  heap = []

  # add the first k elements into the heap
  for i in range(k):
    heappush(heap, nums[i])

  # go through the rest of the array and check if the top of the heap is less than the current element
    # if so pop and then push the new element into the heap
  for i in range(k, len(nums)):
    if heap[0] < nums[i]:
      heappop(heap)
      heappush(heap, nums[i])

  # return the heap as a list, which is size k and has the k highest elements

  return list(heap)
  
  
 # O(N * logk) time complexity, where N is the length of the given array and k is the number of elements that we need to return. We traverse through the array once and do not repeat any calculations. It takes logK time to remove the smallest number from our minheap.
 # O(k) space complexity since we keep out heap to size k.
