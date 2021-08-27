# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        we are given two linkedlists
            we can use dummy head to build the combined list
                one pointer on one linkedlist and another on the other linkedlist
                we compare the value at each and then insert the smaller one       
        """
        
        dummy = None
        tail = None
        
        # compare the values and build the linkedlist
        while l1 and l2:
            
            if l1.val >= l2.val:
                
                # get the head of the result list here if possible, can only enter at most once it not below
                if dummy is None:
                    dummy = l2
                    tail = dummy
                else:
                    tail.next = l2
                    tail = tail.next
                    
                l2 = l2.next
                    
            else:
                
                # get the head of the result list here if possible, can only enter at most once if not above
                if dummy is None:
                    dummy = l1
                    tail = dummy
                else:
                    tail.next = l1
                    tail = tail.next
                    
                l1 = l1.next
                
        # if we hit the end of one list just add the rest of the other list
        if l1 is None:
            
            # if l1 was always empty
            if dummy is None:
                dummy = l2
            # add the rest of the list
            else:
                tail.next = l2
                
        else:
            
            # if l2 is always empty
            if dummy is None:
                dummy = l1
            # add the rest of the list
            else:
                tail.next = l1
        
        return dummy
        
# O(N + M) time complexity, where N and M are the lengths of the given linkedlists. We traverse through each linkedlist once.
# O(N + M) space complexity since we are combining the lists and that is our output.
