# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
U
have have k linkedlists
we return a linkedlist with every element of the k linkedlists in nondecreasing order
    there can be duplicate numbers 

we are not given k

if the linkedlist is empty return an empty list => None

M
first thought is combine everything and sort but we already have each linkedlist sorted so thats not efficient

heap
    we can use a heap to pick the smallest element and add it to the combined linkedlist that we want to return
smallest numbers get popped first so min heap

heap is size k
we have k linkedlists so thats like k pointers
the nice part about linkedlist is that we dont have to keep track of which list and position since the node class handles that

P
# we dont need it: find k which should be the length of the given lists

go through each of the lists and push each head if it is not None to the heap

then we pop and add to our result linkedlist
    we then push the next element into our heap

once our heap is empty, then we know we are done

return the head of our combined result linkedlist

I
See solution class below

R
lists = [[1,4,5],[1,3,4],[2,6]]

k = 3 bc that is the length of lists

[
  1->4->5,
  1->3->4,
  2->6
]

heap will have 1,1,2
result: None

heap will have 4,1,2
result: 1

heap will have 4,3,2
result: 1 -> 1

heap will have 4,3,6
result: 1 -> 1 -> 2

and so on

E
O(Nlogk) time complexity since we visit each element in all of the linked list once and size k heap takes logk time to reblance
O(k) space complexity since our heap is size k.
"""
from heapq import *

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        """
        # issue: < is not supported by out custom class so we will have to override the "<" operator in our node class
            # i dont have access to it so I will have to use a lambda inside the solution class
        
        def __lt__(self, other):
            self.val < other.val
        
        """
        ListNode.__lt__ = lambda self, other: self.val < other.val
                
        k = len(lists)      
        min_heap = []

        for head in lists:
            if head is not None:
                heappush(min_heap, head)

        resultHead = None
        resultTail = None
        
        while min_heap:
            curr_node = heappop(min_heap)
            
            # first node of our result
            if resultHead is None:
                resultHead = curr_node
                resultTail = resultHead
            # every node after
            else:
                resultTail.next = curr_node
                resultTail = resultTail.next
            
            # we won't add None to the heap since that means we are done with the linkedlist that the current node is from
            if curr_node.next is not None:
                heappush(min_heap, curr_node.next)

        return resultHead


      
      
"""

Below is the case when I write my own node class

"""      
      

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
