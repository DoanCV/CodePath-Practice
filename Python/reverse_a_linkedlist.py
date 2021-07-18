class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def reverse(head):
  prev = None
  curr = head
  while curr is not None:
    # store the next node to safely reverse current node
    temp = curr.next
    # reverse the current node 
    curr.next = prev
    
    # make previous node the current node to go onto the next node
    prev = curr
    curr = temp
  return prev

# O(N) time complexity, where N is the number of nodes in the given linkedlist. We solve the problem in one pass through the linkedlist.
# O(1) space complexity since we only use auxillary space by storing the next node as temp.
