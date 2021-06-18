class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next


def find_middle_of_linked_list(head):
  """ fast and slow pointer since we want to find the answer in one iteration, another approach would be to iteratoe once to count the length then find the middle one in the next iteration
  if the fast pointer reaches the end that means the slow pointer is at the middle since one moves twice as fast
  """
  hare = head
  tortoise = head

  while hare is not None and hare.next is not None:
    hare = hare.next.next
    tortoise = tortoise.next
  return tortoise

# O(N) time complexity, where N is the length of the linkedlist, since we pass through the length of the linkedlist once.
# O(1) space complexity since we are not using new data structures.
