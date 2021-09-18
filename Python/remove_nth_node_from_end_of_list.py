# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
U
Return the given linkedlist without the nth from the end node


M
Singly Linkedlist problem

approach:
Multi pass to get the length of the linkedlist and then you can remove the 

approach:
Two pointer + dummy head approach

dummy head will make it easy to remove the head for the edge case where N is the size of the linkedlist
keep two pointers N nodes apart


P
we will go with the second approach

initialize a dummy head to an arbitrary value
    start two pointers here
move one pointer N nodes away from the other pointer

now that they are N apart move both one at a time until the one is further out is at the end
the next node after the start pointer is the node we need to remove
    so just skip it when we link

return dummy.next since that is the head of our linkedlist without the node we just removed

I
"""
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyHead = ListNode(-1)
        dummyHead.next = head
        start = n_from_start = dummyHead
        
        for _ in range(n):
            n_from_start = n_from_start.next
        
        while n_from_start.next:
            n_from_start = n_from_start.next
            start = start.next
        
        start.next = start.next.next
        
        return dummyHead.next
    
"""
R
n = 2
Dummy -> 1 -> 2 -> 3 -> 4 -> 5

start
end

then,

start
            end

then,
                 start
                            end

E
O(N) time complexity where N is the length of our given linkedlist since we solve in one pass
O(1) space complexity since we solve in place
"""
