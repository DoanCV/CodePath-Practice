# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
We are given a binary tree find the longest zigzag path
    the path can start from anywhere and end anywhere
    the idea is that if we go left then we go right and the otherway around, basically just alternate

We can keep track of the direction change and the number of steps so far

I see two ways to do this:

Recursive DFS
Try to go right and then left
    If we went past a leaf node then we stop search here
    else
        update the max
        
        if we just went right
            go left and increment path length
            go right and reset to start a search starting from here
        if we just went left
            go right and increment path length
            go left and reset to start a search starting from here

O(N) time complexity where N is the number of nodes in the given binary tree since we visit every node once.
O(height) space complexity since our recursive call stack is worst case as deep as the tree is which can be thought of as the height.



Iterative BFS
use a queue
    we store (the node, the direction it came from so left or right, the path length so far)
    add the root twice but from different directions to start the search with path length 0
 
while the queue is not empty
    pop the queue
    update the max
    
    if there is a left child
        go left and if the last direction was left reset the path length to start the search from here
        go left and if the last direction was right increment path length
        
    if there is a right child
        go right and if the last direction was right reset the path length to start the search from here
        go right and if the last direction was left increment path length

O(N) time complexity where N is the number of nodes in the given binary tree. We visit every node once, we access the node twice since if possible we try to branch out in two directions. This is still a linear time traversal. 
O(N) space complexity since we use a queue to keep track of a level at a time. A level in the worst case is N/2 since we have a full bottom level. One level above we wouldve tried two directions both each node so that is N.
"""
### Iterative BFS
from collections import deque
class Solution:   
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        
        max_path_len = 0
        
        if root is None:
            return max_path_len
        
        queue = deque()
        queue.append((root, "left", 0))
        queue.append((root, "right", 0))
        
        while queue:
            
            node, last_move, path_len = queue.popleft()
            
            max_path_len = max(max_path_len, path_len)
            
            if node.left:
                if last_move == "left":
                    queue.append((node.left, "left", 1))
                if last_move == "right":
                    queue.append((node.left, "left", path_len + 1))
                
            if node.right:
                if last_move == "left":
                    queue.append((node.right, "right", path_len + 1))
                if last_move == "right":
                    queue.append((node.right, "right", 1))
                    
        return max_path_len
        
        
### Recursive DFS
class Solution:
    
    max_path_len = 0
    
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
                
        self.zigzag(root, True, 0)
        self.zigzag(root, False, 0)
        
        return self.max_path_len
    
    def zigzag(self, node, isLeft, steps):
            
            if node is None:
                return
            
            self.max_path_len = max(self.max_path_len, steps)
            
            if isLeft:
                self.zigzag(node.left, False, steps + 1)
                self.zigzag(node.right, True, 1)
                
            else:
                self.zigzag(node.right, True, steps + 1)
                self.zigzag(node.left, False, 1)
