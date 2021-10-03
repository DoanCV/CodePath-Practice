# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
U
we are given a binary tree (root)

we need to invert and return the root
    inverting means to swap the children nodes

M
tree traversal
    DFS with recursion
    
we can use preorder
    visit 
    left
    right

P
use a helper function
    we will feed in a node and then swap the left and right
    then feed the left and right child for the next call

IRE
"""

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        
        self.dfs(root)
        
        return root
    
    def dfs(self, node):
        if node is None:
            return
        
        node.right, node.left = node.left, node.right
        
        self.dfs(node.left)
        self.dfs(node.right)
