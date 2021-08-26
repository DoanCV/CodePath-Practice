from heapq import *

class ListNode:
  def __init__(self, value):
    self.value = value
    self.next = None

  # we need to override the "<" since we are using a node class
  def __lt__(self, other):
    return self.value < other.value

"""
brute force: concat every linkedlist then sort

optimal:
We will use minheap to store the smallest element of each linkedlist
  then we pop and put that element into the result
    when we pop we have to move to the next element of the respective linkedlist
      if we are at the end of the list do not add anything
    then we add that element to the heap

when our heap is empty we know that we have visited all elements

return the head of the result linkedlist
  we can use dummy head and keep track of the result linkedlist tail
"""

def merge_lists(lists):
  heap = []

  # add head nodes into the heap
  for head in lists:
    if head is not None:
      heappush(heap, head)

  # while the heap is not empty we will do what i outlined above
  resultHead = None
  resultTail = None
  while heap:

    # get the smallest value
    curr_node = heappop(heap)

    # use a dummy head
    if resultHead is None:
      resultHead = curr_node
      resultTail = curr_node
    # move the tail
    else:
      resultTail.next = curr_node
      resultTail = resultTail.next
    
    # add the next node in the current linkedlist into the heap
    if curr_node.next is not None:
      heappush(heap, curr_node.next)

  return resultHead

# O(Nlogk) time complexity, where N is the total length of all the given linkedlists and k is the number of linkedlists. We visit every node once and we pop from a size k min heap.
# O(k) space complexity since our heap has a size of k.
