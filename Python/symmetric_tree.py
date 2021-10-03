# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
U
we are given a binary tree

return True if it is symmetrical around its center else return False

a tree is symmetrical about its center when the values over the reflection are equal

M
tree traversal to verify symmetry
    DFS with recursion

we need to check if the position is reflected

for example
            1
        /        \
        2         2
     /    \     /    \
    3      4   4      3
is symmetrical
the left of 1 is equal to the right of 1
    the left of 2 is equal to the right of 2
    the right of 2 is equal to the left of 2
    
            1
        /        \
        2         2
         \         \
          3         3
is not symmetrical since the left of one 2 is not the same as the right of the other 2

compare
    left nodes' left with right node's right
    left nodes' right with right node's left


P
we will use a helper function to compare the right and left


IRE

"""


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        return self.recurse(root.left, root.right)
    
    def recurse(self, left, right):
        # check if None
            # if only one is None then not symmetric
            # if both then symmetric
            
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        
        
        # if the values are not the same then not symmetric
        if left.val != right.val:
            return False
        
        # left nodes' left with right node's right
        # left nodes' right with right node's left
        
        return self.recurse(left.left, right.right) and self.recurse(left.right, right.left)
