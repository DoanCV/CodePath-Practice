# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
U
Given a binary tree determine if it is height balanced
    the height is the number of nodes from the root

left and right subtrees cant differ in height by more than 1

M
we can check the depth of the right and left subtree and see if they differ by more than 1 with recursion
    we use the depth since we are given the root

postorder traversal
since we get the heights of the subtree then check for validity


P
we will use a helper function to find the max depth
    if we have a null node return 0
    
    use a flag to denote not balanced (-1)
    
    if the flag is -1 then return -1 up the call stack or if the left and right subtree height differ by more than 1 then also return -1
    # the difference in height is equal to the difference in depth
    
    get the max depth of each subtree by adding 1 for each recursive depth
    
    
IRE
"""

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        return self.recurse(root) != -1

    
    def recurse(self, node):
        if node is None:
            return 0
        
        left = self.recurse(node.left)
        right = self.recurse(node.right)
        
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1 
        
        return max(left, right) + 1
