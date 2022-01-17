# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        
        Find the middle of the linkedlist
        Reverse the second half of the linkedlist
        Merge the two halves
        """
        
        if not head:
            return []
        
        # get to the middle
        fast = head
        slow = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse the 2nd half and split the 2nd half from the 1st half
        prev = None
        curr = slow.next
        while curr:
            temp = curr.next
            curr.next = prev
            
            prev = curr
            curr = temp
            
        slow.next = None
        
        # merge the two linkedlists
            # the two halves will either have the same number of nodes or the 1st half will have one more 
        head1 = head
        head2 = prev
        while head2:
            temp = head1.next
            head1.next = head2
            head1 = head2
            head2 = temp
