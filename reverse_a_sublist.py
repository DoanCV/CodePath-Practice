class Node:
  def __init__(self, value, next = None):
    self.value = value
    self.next = next

""" p = 2, q = 4
1 -> 2 -> 3 -> 4 -> 5 -> null
node p now points to node q + 1
node p + 1 now points to p
...
node q points to q - 1
...
1 -> 2 ---------
               |
     3 -> 4 -> 5 -> null
reverse the rest normally

1 -> 2 ------------
     ^             | 
     |-- 3    4 -> 5 -> null

1 -> 2 ------------
     ^             | 
     |-- 3 <- 4    5 -> null

1 -> 2 ------------
     ^             | 
     |-- 3 <- 4    5 -> null

1 -> 4 -> 3 -> 2 -> 5 -> null

logic:
# if p is equal to q, we don't need to do anything, return head
# p and q are positional
curr = head

# skip to p, save p-1
i = 0
while curr is not None and i < p-1:
    prev = curr
    curr = curr.next
    i += 1
end_of_pre_sub = prev
end_of_sub_list = curr

# reverse p through q normally
j = 0
while curr is not None and j < q - p + 1:
  temp = curr.next
  curr.next = prev

  prev = curr
  curr = temp
  j += 1

# connect q+1 and p-1
  # the last node before sublist should point to the last node of the original sublist
  # we need to check if p is 1 since that means there is no pre sublist and that means the head has to be the last node of the original sublist
  end_of_pre_sub.next = prev

# the first node of teh orginal sublist should point to the q + 1
end_of_sub_list = curr

"""

def reverse_sub_list(head, p, q):
  if p == q:
    return head
  
  curr = head
  i = 0
  while curr is not None and i < p - 1:
    prev = curr
    curr = curr.next
    i += 1

  end_of_pre_sub = prev
  end_of_sub_list = curr

  j = 0
  while curr is not None and j < q - p + 1:
    temp = curr.next
    curr.next = prev
    prev = curr
    curr = temp
    j += 1
  
  if end_of_pre_sub is not None:
    end_of_pre_sub.next = prev
  else:
    head = prev

  end_of_sub_list.next = curr
  
  return head

# O(N) time complexity, where N is the number of nodes in the given linkedlist, since the sublist might be the entire linkedlist.
# O(1) space complexity since we are not using any more data strucutres. This the reversal of the linkedlist is an in place operation.
