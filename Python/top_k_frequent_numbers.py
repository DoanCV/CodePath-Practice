from heapq import *

def find_k_frequent_numbers(nums, k):
  """
  we need to keep track of the frequencey of each number
    use hashmap
  
  use a min heap storing (the number, its frequency)
    we insert until we have k
    then if there is a frequency higher than the top of the heap we pop and then push the new value and rebalance
  
  then we get the numbers from the size k heap and return them
    we need to index the tuple
  """
  topNumbers = []

  frequencies = {}
  for i in range(len(nums)):
    if nums[i] not in frequencies:
      frequencies[nums[i]] = 0
    frequencies[nums[i]] += 1
  
  min_heap = []
  for key, value in frequencies.items():
    heappush(min_heap, (value, key))
    if len(min_heap) > k:
      heappop(min_heap)
  
  for curr in range(len(min_heap)):
    value, key = heappop(min_heap)
    topNumbers.append(key)

  return topNumbers
  
  
# O(Nlogk + N) time complexity, where N is the length of the given array and k is given. We store the element and its frequency in a hashmap in one traversal. Then we add the key, value pairs into a minheap. While doing so if our min heap exceed a size of k we pop and rebalance. It takes logk time to extract the top element from a size k heap and rebalance. In the worst case, every number is unique. I keep N + Nlogk since we dont know how big k is, just that it wont be bigger than N.
# O(N) space complexity since our hash map of frequencies in the worst case is size N since nums can have all unique values. K will never be larger than N so even with our heap it is still N.
