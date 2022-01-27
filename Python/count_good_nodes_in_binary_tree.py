# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
U
a node is good if in the path from root to the node has no nodes that have a greater value
    so if the node is at least the max of its ancestor then it is good

M
preorder DFS

P
we need to pass the maximum so far at each step in our recursion
if the value of the current node is greater than or equal to its previosuly seen max
    the current node is a good node

a null node value is 0
"""

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        
        def dfs(curr_node, curr_value):
            
            if not curr_node:
                return 0
            
            max_path_value = max(curr_node.val, curr_value)
            
            return (curr_node.val >= max_path_value) + dfs(curr_node.left, max_path_value) + dfs(curr_node.right, max_path_value)
            
        return dfs(root, root.val)
