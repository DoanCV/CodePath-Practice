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

# O(N) time complexity, where N is the length of given linked list.
# O(1) space complexity.
