"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

"""
traverse through the linkedlist starting with the head

when the current node with a child we know that all the nodes in this branch will come before the node following the current node
    there are multiple levels so to keep the order in which we connect a level we will store the next node in a stack

stack is not mandatory though

i can just link the tail of the immediate child to the next node after the current node
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        
        if head is None:
            return None
        
        curr = head
        
        while curr:
            
            # case 1: current node does not have child
            if curr.child is None:
                curr = curr.next
                continue
            
            # case 2: current node has a child so we must flatten
            temp = curr.child
                        
            # get the child and find its tail 
            while temp.next:
                temp = temp.next
            
            # connect the tail to the current.next of the level above and make current.next the child of current
            # then remove the child from curr.child
            temp.next = curr.next
            
            # edge case: if curr is already at the end of the linkedlist then None.prev wont make sense
            if curr.next:
                curr.next.prev = temp
            
            curr.next = curr.child
            curr.child.prev = curr
            curr.child = None
        
        return head
            
