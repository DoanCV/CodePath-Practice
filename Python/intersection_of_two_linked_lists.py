# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""
U
Given two linkedlists find if they intersect and return the node where they intersect 

input: the heads of each linkedlist
output: the node that the two linkedlist intersects or None

the given test cases seem like they are enough
    when we have empty list, at least one we will return null
    
M
No extra space is needed

P
We will have two pointers, one will start at headA and the other will start at headB

while they are not the same we will move both pointers
    if one reaches the end we will move that one to the head of the other linkedlist
    
when the two meet we just return one of the nodes since that is where the linkedlists intersect

I
See class below

R


E 
O(N) time complexity since we solve in worst case two passes
O(1) space complexity since we are solving in place

"""
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        if headA is None or headB is None:
            return None
        
        ptr1 = headA
        ptr2 = headB
        
        while ptr1 != ptr2:
            
            if ptr1 is None:
                ptr1 = headB
            else:
                ptr1 = ptr1.next
            
            if ptr2 is None:
                ptr2 = headA
            else:
                ptr2 = ptr2.next
                
        return ptr1
            
"""
Tortoise and hare approach
"""
        
# Note that this function should return a ListNode, not an int
def getIntersectionNode(list1, list2):
    if not list1 or not list2:
        return None
    
    tail1 = list1
    while tail1.next is not None:
        tail1 = tail1.next
    tail1.next = list2
    
    hare = list1
    tortoise = list1
    
    while True:
        if not hare.next or not hare.next.next:
            tail1.next = None
            return None
        else:
            tortoise = tortoise.next
            hare = hare.next.next
            if hare == tortoise:
                hare = list1
                break
                
    while hare != tortoise:
        hare = hare.next
        tortoise = tortoise.next
    
    tail1.next = None
    return hare
