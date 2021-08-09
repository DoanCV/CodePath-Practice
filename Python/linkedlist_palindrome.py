# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        Linear time:
        traverse once to add all nodes to a stack
        traverse a second time and for each node, pop from stack and compare
        
        we can do better
        
        Constant space:
        reverse the second half of the linkedlist
        traverse through both halves and compare
        """
        
        fast = head
        slow = head
        
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
        
        # now our slow is at the middle and our fast is at the end
            # we need to reverse but we can create a helper function to keep isPalindrome less cluttered
        
        second_half = self.reverseLinkedList(slow)
        
        # start from the beginning of original half (its called fast but i will traverse one node at a time, i just dont want to leave fast from before hanging)
        first_half = head
    
        while second_half != None:
            print(first_half.val)
            print(second_half.val)
            if first_half.val != second_half.val:
                return False
            
            first_half = first_half.next
            second_half = second_half.next
        
        return True
    
    def reverseLinkedList(self, curr):
        prev = None
        while curr != None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
