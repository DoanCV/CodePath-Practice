
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


"""
BFS since we need to link nodes in each level
    the rightmost node on each level will point to None
    
we will do this iteratively, with a queue
    add the root

while the queue is not empty
    
    link popped node to what is next to pop from the queue
        at the end of the iteration we know we are on the last node of the level so .next is None
        add the children of the nodes
    add None back to the queue to denote the end of the level
    
"""
from collections import deque
class Solution:
    def connect_BFS(self, root):
        if root is None:
            return None
        
        
        queue = deque()
        queue.append(root)
        queue.append(None) # this way we can root.next = queue[0] and use this for every other level
        
        while queue:
            curr_node = queue.popleft()
            
            if curr_node is not None:
                curr_node.next = queue[0]
                
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
                    
            # mark the end of each level
            else:
                if len(queue) > 0:
                    queue.append(None)
                    
        return root

"""
Literally the same solution for Populating Next Right Pointers in Each Node works for Populating Next Right Pointers in Each Node II
    the thing is we still take O(N) time and O(N) space
        in both problems we can solve with O(1) space

For O(1) space we treat each level like a linkedlist and we use a dummy head between levels

node is for the current level
we have a dummy head
dummyHead.next: let dummy head's next store the first node of the child level for us;
dummyTail is for the child level traversal, to connect each node in child level while moving ahead.
        
When this level's work are all done, we move to next level by: 
    root = dummyHead.next      # Just the child level's head
    dummyTail = prekid         # We use this dummy head for the new level's traversal.
    dummyTail.next = None      # Let the dummy head's next be None, before we going for this new level.

"""
### Constant space solution
class otherSolution:
    def connect(self, root):
        
        node = root
        dummyHead = Node(0)
        dummyTail = dummyHead
        while node:
            
            while node:
                
                if node.left:
                    dummyTail.next = node.left
                    dummyTail = dummyTail.next
                if node.right:
                    dummyTail.next = node.right
                    dummyTail = dummyTail.next
                node = node.next
                
                
            node = dummyHead.next
            dummyTail = dummyHead
            dummyTail.next = None
            
        return root
        
