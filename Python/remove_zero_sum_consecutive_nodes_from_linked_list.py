"""
Given the head of a linkedlist, delete consecutive sequences of nodes that sum to zero until there are no longer such sequences


Solve in two passes
    - First pass: Calculate prefix sum and save to hashmap
    - Seocnd pass: Calculcate prefix sum and skip to the last instance of the prefix sum in the hashmap
    
we need a dummy head to have a prefix sum of 0 that way we return None with dummy_head.next
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        last_seen = {}
        
        dummy_head = ListNode(0)
        dummy_head.next = head
        
        last_seen[0] = dummy_head
        
        prefix_sum = 0
        while head:
            prefix_sum += head.val
            last_seen[prefix_sum] = head
            head = head.next
            
        head = dummy_head # [1,-1] -> []
        prefix_sum = 0
        while head:
            prefix_sum += head.val
            head.next = last_seen[prefix_sum].next
            head = head.next

        return dummy_head.next
