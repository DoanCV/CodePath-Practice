# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # reverse
        l1_head = self.reverse_list(l1)
        l2_head = self.reverse_list(l2)
        
        remainder = 0
        dummy_head = None
        dummy_tail = None
        while l1_head and l2_head:
            digit_sum = (l1_head.val + l2_head.val + remainder) % 10
            remainder = (l1_head.val + l2_head.val + remainder) // 10
            
            if dummy_head is None:
                dummy_tail = ListNode(digit_sum)
                dummy_head = dummy_tail
            else:
                dummy_tail.next = ListNode(digit_sum)
                dummy_tail = dummy_tail.next
            
            l1_head = l1_head.next
            l2_head = l2_head.next
        
        while l1_head:
            digit_sum = (l1_head.val + remainder) % 10
            remainder = (l1_head.val + remainder) // 10
            dummy_tail.next = ListNode(digit_sum)
            dummy_tail = dummy_tail.next
            l1_head = l1_head.next
            
        while l2_head:
            digit_sum = (l2_head.val + remainder) % 10
            remainder = (l2_head.val + remainder) // 10
            dummy_tail.next = ListNode(digit_sum)
            dummy_tail = dummy_tail.next
            l2_head = l2_head.next
        
        if remainder > 0:
            dummy_tail.next = ListNode(remainder)
            dummy_tail = dummy_tail.next
            
        return self.reverse_list(dummy_head)
        
    def reverse_list(self, head):
        curr = head
        prev = None
        
        while curr:
            temp = curr.next
            curr.next = prev
            
            prev = curr
            curr = temp
        
        return prev
