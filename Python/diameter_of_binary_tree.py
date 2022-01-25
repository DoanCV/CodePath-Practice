# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
given thre root of a binary tree, return its diameter
    the diameter is the length of the longest path between any two nodes in a tree
    the path may or may not pass through the root
    

we can just find the maximum depth of the subtrees and add them together
    the deeper subtree should be passed up the recursion since that is potentially part of the best answer

"""
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.max = 0
        self.dfs(root)
        
        return self.max
    
    def dfs(self, node):
        if not node:
            return 0
        
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        
        self.max = max(self.max, left + right)
        
        return max(left, right) + 1
