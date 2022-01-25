# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        dummy_head = ListNode(-1)
        dummy_head.next = head
        
        curr = dummy_head # start from the dumym head since that way we do not have to wrote more code for edge cases
        while curr.next:
            
            if curr.next.val == val: # skip the next node if it its value is the value we need to remove
                curr.next = curr.next.next
            else:
                curr = curr.next
            
        return dummy_head.next
