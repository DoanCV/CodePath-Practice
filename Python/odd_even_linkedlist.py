# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        linear space:
        we can make a new list and add the evens then connect the odds. when we have the two lists connect the end of the odds to the start of the evens
        
        constant space:
        everything must be done in place, we wont be creating another list
        
        we know that the odds and evens alternate 
        as long as we connect odds together and the evens together in one traversal we can connect the end of the odd connections to the start of the evens
        """
        
        # check if the list is empty
        if head is None:
            return None
        
        # keep track of the even, odd and start of even nodes
        odd = head
        even = head.next
        even_start = head.next
        
        while even is not None and even.next is not None:
            # the next odd is the node adjacent to the even one since they alternate
            odd.next = even.next
            # update odd for next iteration
            odd = odd.next
            
            # same idea but for the even nodes
            even.next = odd.next
            even = even.next
            
        # we need to connect the odds to the start of the evens
        # we already reached the end of the odds, the start of the evens we already determined at the beginning
        odd.next = even_start
        
        return head
      
# O(N) time complexity, where N is the number of nodes in the given linkedlist, since we solve in one loop.
# O(1) space complexity since we solve in place.
