# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        """
        store tuple (value, index) in a stack to pop in constant time
        if the current value is greater than the last value of the stack 
            we pop and make the current value the value at the index from the popped tuple
        
        """
        result = []
        stack = []
        curr_index = 0
        while head:
            result.append(0)
            curr = head.val
            while stack and stack[-1][0] < curr:
                _, popped_index = stack.pop()
                result[popped_index] = curr
            
            stack.append((curr, curr_index))
            curr_index += 1
            head = head.next
        return result
 
 # O(N) time complexity, where N is the number of nodes in the given linkedlist, since we solve in one pass of the linkedlist.
 # O(N) space complexity since we use a stack and in the worst case we pop nothing from the stack since there are no next largest node.
