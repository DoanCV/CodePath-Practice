# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
U
we do not have the head
we are given the node to delete

the given test cases are enough
    empty list, doesnt make sense there would be nothing to delete
    duplicate nodes? delete all or delete just one

M
we do not need any space

P
# delete
apparently we cant actaully delete, just copy the value of the node that follows the node to delete and then skip two nodes

### NOTE: we arent given the head otherwise I would store previous in a loop and manipulate when i find the node

I

R
It works but I am afraid if I was not using Python we could have memory leak since we dont free the memory of the node we skipped

E
Constant
O(1)
"""

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        
        node.val = node.next.val
        node.next = node.next.next
