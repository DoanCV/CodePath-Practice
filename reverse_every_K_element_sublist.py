class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next


def reverse_every_k_elements(head, k):
  if head is None or k <= 1:
    return head
  
  curr = head
  prev = None
  while True:
    end_of_pre_sublist = prev
    end_of_new_sublist = curr

    i = 0
    while i < k and curr is not None:
      temp = curr.next
      curr.next = prev
      
      prev = curr
      curr = temp
      i += 1
    
    if end_of_pre_sublist is not None:
      end_of_pre_sublist.next = prev
    else:
      head = prev
    
    end_of_new_sublist.next = curr

    if curr is None:
      break
    
    prev = end_of_new_sublist

  return head

# O(N) time complexity, where N is the number of nodes in the given linkedlist, since we solve in one pass through the entire linkedlist.
# O(1) space complexity since we are not using extra data structures.
