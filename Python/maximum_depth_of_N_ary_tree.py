from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        """
        Iterative BFS - use a queue
         
        we will push the children of each node at a level and the depth + 1 into the queue
        """
        
        max_depth = 0
        
        if root is None:
            return max_depth
        
        queue = deque()
        queue.append((root, 1))
        
        while queue:
            curr_node, depth = queue.pop()
            
            for child_node in curr_node.children:
                if child_node is not None:
                    queue.append( (child_node, depth + 1) )
            
            max_depth = max(depth, max_depth)
        
        return max_depth
