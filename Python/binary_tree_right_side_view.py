# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
We are standing on the right side of the tree. Return the value of the nodes that I can see in top to bottom order.
    Keep in mind that the answer is not simply the right side of the tree or at least we need to define what that means
    If we have a left heavy tree we will of course see nodes that are in a left subtree but are still on the right
        this will apply to every depth
        we have to look for the rightmost node at each depth
        
First thought BFS
    We can use a queue to iteratively traverse level by level and only store the rightmmost node at each level in a results list which in the end hold our answer

Second thought DFS
    We can use a modified inorder traversal by visiting right node left rather than left node right
    We store the node values in a hashmap = {depth: value}
    The first node we encounter at a depth will be the rightmost node since we are using modified inorder traversal

O(N) time complexity where N is the number of nodes in the given binary tree since we visit each node once.
O(N) space complexity since we use a queue to hold the nodes of a level. In the worst case the bottom level is size N/2 which grows linearly with N.
"""
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        right_side_view = []
        
        if root is None:
            return right_side_view
        
        queue = deque()
        queue.append(root)
        
        while queue:
            
            level_len = len(queue)
            
            for _ in range(level_len):
                curr_node = queue.popleft()
                right_most_node = curr_node
                
                if curr_node.left:
                    queue.append(curr_node.left)
                
                if curr_node.right:
                    queue.append(curr_node.right)
            
            right_side_view.append(right_most_node.val)
        
        return right_side_view
