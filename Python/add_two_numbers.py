# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
U
The two given linkedlists are not empty
    they are also not guaranteed to be the same size
    no negative values

the numbers are given in rever order which is good
    it flows with normal addition or at least how I do addition

the given cases cover enough for me

M
we can simply add the values one level at a time

we do need memory to create the linkedlist storing each digit of the sum

to deal with carry over we will need to keep track of the sum beyond 10 since 0-9 we can store

P

keep two pointers, one that starts at the head of one linkedlist and another that starts at the other linkedlist

while we are not at the end of the list we will need to 


when we reached the end of one list then we have to continue with the remainder of the other list
however we still need to deal with carry
once we are done we can just attach the remainder of the linkedlist since we have nothing to add

I
See solution class below

R
243
564

7 -> 0 -> 8

2 + 5 = 7
7 % 10 = 7
7 // 10 = 0
we carry nothing over
the digit we build is 7

4 + 6 = 10
10 % 10 = 0
10 // 10 = 1
we carry 1 over
and the digit we build is 0

3 + 4 + 1 = 8
8 % 10 = 8
8 // 10 = 0
we carry nothing over
the digit we build is 8


E

"""

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        ptr1 = l1
        ptr2 = l2
        
        sum_head = None
        sum_tail = None
        
        carry = 0
        
        while ptr1 is not None and ptr2 is not None:
            
            place_sum = ptr1.val + ptr2.val + carry
            
            digit = place_sum % 10
            
            carry = place_sum // 10
            
            if sum_head is None:
                sum_tail = ListNode(digit)
                sum_head = sum_tail
            else:
                sum_tail.next = ListNode(digit)
                sum_tail = sum_tail.next
            
            # continue to the next place (digit)
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        
        # check which linkedlist is not finished and add the rest but keep in mind carry 
        while ptr1 is not None:
            place_sum = ptr1.val + carry
            digit = place_sum % 10
            carry = place_sum // 10
            sum_tail.next = ListNode(digit)
            sum_tail = sum_tail.next
            ptr1 = ptr1.next
        
        while ptr2 is not None:
            place_sum = ptr2.val + carry
            digit = place_sum % 10
            carry = place_sum // 10
            sum_tail.next = ListNode(digit)
            sum_tail = sum_tail.next
            ptr2 = ptr2.next
        
        # fill the remainder after we deal with any carry
        if carry > 0:
            sum_tail.next = ListNode(carry)
        
        return sum_head
