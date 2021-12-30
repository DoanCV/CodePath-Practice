# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head or left == right:
            return head
        
        # dummy head to easily return the head of new linkedlist
        dummy = ListNode(None)
        dummy.next = head
        
        # go up to the node right before the left of the range, keep in mind nodes are indexed from 1 as given in the examples
        start = dummy
        for _ in range(left - 1):
            start = start.next

        curr = start.next
        prev = None
        for _ in range(right - left + 1):
            
            temp = curr.next
            curr.next = prev
            
            prev = curr
            curr = temp
        
        # 1 -> 2 <- 3 <- 4 5
            # curr = 5
            # start = 1
            # prev = 4
        start.next.next = curr
        start.next = prev
        # 1 -> 4 -> 3 -> 2 -> 5
        
        return dummy.next
