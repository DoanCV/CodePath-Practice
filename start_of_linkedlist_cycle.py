class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.value, end='')
      temp = temp.next
    print()


def find_cycle_start(head):
  hare = head
  tortoise = head

  while hare is not None and tortoise is not None:
    hare = hare.next.next
    tortoise = tortoise.next
    if hare == tortoise:
      cycle_length = find_cycle_length(tortoise)
      break
  return find_start(cycle_length, head)
  
def find_cycle_length(tortoise):
  curr = tortoise
  length = 0
  while True:
    curr = curr.next
    length += 1
    if curr == tortoise:
      return length

def find_start(cycle_length, head):
  ptr1 = head
  ptr2 = head
  while cycle_length > 0:
    ptr2.next
    cycle_length -= 1

  while ptr1 != ptr2:
    ptr1 = ptr1.next
    ptr2 = ptr2.next
  return ptr1

# O(N) time complexity, where N is the length of the given linkedlist. The N is simplified from 2N or N + N. 
  # To find the length of the cycle we need N computational steps worst case. Let's call this length k.
  # We move ptr2 k nodes and then increment both ptr1 and ptr2 one node at a time until they meet. They will meet at the start of the cycle and ptr2 would have completed one cycle.
# O(1) space complexity since we are not creating any new data structures to calculate our answer.
