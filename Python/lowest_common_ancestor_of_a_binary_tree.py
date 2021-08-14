# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        # Post Order Recursive DFS 
        # a node can be a descendant of itself so we will check the children first then visit the node
        # we are looking for the lowest so that means "higher up"
        
        # no need to recurse if 
            # None
            # node is p or q 
        
        # post order (left, right, visit)
        # look for the common ancestor
        left = go left
        right = go right
        
        # visit
            # if left and right are both none there is no answer
            # if both have ancestor then the current is the ancestor
            # if one then just return that one
        
        """
        
        if root == p or root == q or root is None:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left is None and right is None:
            return None
        elif left is not None and right is not None:
            return root
        elif left is not None and right is None:
            return left
        else:
            return right
 
# O(N) time complexity, where N is the number of nodes in the binary tree, since we visit each node once.
# O(N) space complexity for the recursive call stack.
