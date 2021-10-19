# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        check the range given the value of the current node
            we know all nodes in the left subtree must be less than its root and right subtree must be greater than its root
        
        iterative dfs - use a stack
        
        the stack will contain (a node, lower bound, upper bound)
        
        the lower and upper bounds are one less and one more than the given range if inf isnt allowed 
        as long as the stack is not empty
            pop and see if it is within the range inclusive
            if not in the range return False
            
            go left and go right
                append the left node, lower bound and new upper bound to the stack
                append the right node, new lower bound and upper bound to the stack
            
            
        return True
        """
        stack = [(root, -2**31 - 1, 2**31 + 1)]
        
        while stack:
            curr_node, lower_bound, upper_bound = stack.pop()
            
            if not curr_node:
                continue
            
            if curr_node.val <= lower_bound or curr_node.val >= upper_bound:
                return False
            
            stack.append((curr_node.left, lower_bound, curr_node.val))
            stack.append((curr_node.right, curr_node.val, upper_bound))
            
        return True
      
# O(N) time complexity, where N is the number of nodes in the given binary tree, since we visit each node once in our iterative dfs.
# O(N) space complexity since in the worst case we store the maximum amount of nodes on a level in the stack which is proportional to N.
