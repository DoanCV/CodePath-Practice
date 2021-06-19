class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.value, end=" ")
      temp = temp.next
    print()

""" p = 2, q = 4
1 -> 2 -> 3 -> 4 -> 5 -> null
node p now points to node q + 1
node p + 1 now points to p
...

node q points to q - 1
...

1 -> 2 ------------
     |             | 
     --- 3 -> 4 -> 5 -> null
reverse the rest normally



"""
def reverse_sub_list(head, p, q):
  
  return head
