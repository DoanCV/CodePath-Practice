class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next


def has_cycle(head):
  hare = head
  tortoise = head
  while hare is not None and tortoise is not None:
    hare = hare.next.next
    tortoise = tortoise.next
    if hare == tortoise:
      return True
  return False

# O(N) time complexity, where N is the length of the given linkedlist, since the hare will meet the tortoise in the same loop.
# O(1) space complexity, since we are not creating any new data structures.
