# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
U
each time you rotate you move the last node to the front
    we do this k times
    we need to return the list after k rotations
    
k can be really large, even compared to our linkedlist length

M
We can find the length of the linkedlist with a single pass
    this will help us determine how many rotations we actually need

k = k % length of linkedlist
if we rotate length of linkedlist times then we get the original list again so it is pointless

P
we can find the length of the given linkedlist

then we can make the linkedlist circular
    we can do this by pointing the last node to the head

then we go to the (len(linkedlist) - k - 1)st node, watch out for python indexing
    this will be our the tail of our "rotated" linkedlist
        its next node is None
    then the node after, the (len(linkedlist) - k)st node, is the new head

I
See solution class below

R
given: 1 -> 2 -> 3 -> 4 -> 5
k = 2
output: 4 -> 5 -> 1 -> 2 -> 3 -> None

E
O(N) time complexity, where N is the length of our given linkedlist, since we solve in two passes. Each pass is in a linear fashion since we do not repeat calculations.
O(1) space complexity since we solve in place.
"""
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        
        length = 1
        curr = head
        while curr.next:
            curr = curr.next
            length += 1
        
        curr.next = head
        
        k = k % length
        
        temp = head
        for _ in range(length - k - 1):
            temp = temp.next
        
        head = temp.next
        temp.next = None
        
        return head
                   
