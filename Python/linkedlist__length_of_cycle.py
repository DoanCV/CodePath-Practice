class node():
  def __init__(self, value, next = None):
    self.value = value
    self.next = next
    
 def detect_cycle(head):
  hare = head
  tortoise = head
  
  while hare is not None and tortoise is not None:
    hare = hare.next.next
    tortoise = tortoise.next
    
    if hare == tortoise:
      return length_cycle(tortoise)

def length_cycle(tortoise):
  length = 0
  curr = tortoise
  
  while True:
    curr = curr.next
    length += 1
    if curr == tortoise:
      return length

# O(N) time complexity, where N is the length of given linked list, since in the first function, the hare meets the tortoise in the same loop once the tortoise enters the cycle. Then we allow the a copy of the tortoise to travel through the cycle once more to count the length. In the worst case, the cycle is the length of the linkedlist. This is traversing twice in the worst case as well giving us 2N which is still asymptotically N.
# O(1) space complexity since we are not creating new data structures.
