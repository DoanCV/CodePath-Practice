# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        """
        we need to get to the bottom of the tree
        the last level is where we will know how many nodes
        
        we want sublinear 
        
        we can get the height of the tree if we keep going left since the leftmost node of the bottom level is never none
        we then can go to the right and get the height
        
        case 0: empty tree
        
        case 1: if the left and right are equal we can return 2^height - 1 since that is the number of nodes on a perfect complete binary tree of a given height
        case 2: they are not equal so we go to the children and go left and right each
            we check if the heights are the same, if not we repeat, we'll do this recursively 
            for each call we will return 1 + the number of nodes in the left subtree + the number of nodes in the right subtree
        """
        if root is None:
            return 0
        
        return self.dfs(root)
    
    def dfs(self, root):
        if root is None:
            return 0
        
        left_depth = 1
        left = root.left
        while left:
            left = left.left
            left_depth += 1
            
        right_depth = 1
        right = root.right
        while right:
            right = right.right
            right_depth += 1
            
        if left_depth == right_depth:
            return (2**left_depth) - 1
        else:
            left_nodes = self.countNodes(root.left)
            right_nodes = self.countNodes(root.right)
            
            return 1 + left_nodes + right_nodes
        
# O(logN * logN) time complexity, where N is the number of nodes in the given binary tree. The first logN is from the divide an conquer where we split the search in half each time we do not have a depth match. We do this logN times since that is the depth of the binary tree.
# O(1) space complexity if we don't consider recursive call stack.
