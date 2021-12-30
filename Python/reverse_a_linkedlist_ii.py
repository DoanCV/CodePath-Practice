# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head or left == right:
            return head
        
        dummy = ListNode(None)
        dummy.next = head
        
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
        
        start.next.next = curr
        start.next = prev
        
        return dummy.next
