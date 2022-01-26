# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
U
given the root of a binary tree, find the maximum path sum
    a single node can appear once in a path

M
Binary tree recursive DFS

P
Base case
    a single node alone is the max value
    the null nodes have a sum of 0 so that is what we will return in that case
    
if we have a pair of nodes, specifically a positive node and a negative node, we will only choose the positive node
if the entire group of nodes, say the entire tree, are all negatives, the largest node is the answer

this tells us that we care about the gain that we get from a subtree
    so if we get negative gain there is no point to include that in the sum since it doesnt give us the answer

when we explore branches if the sum of all the nodes in the branch is less than 0 we do not count it since it is worthless

since a node can only appear once in a path so can just keep adding and including the subtree sums if the current node itself is not the root of the best answer
    that is why we take keep one subtree when going up the recursive call stack
"""
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_path_sum = float("-inf")
        
        def dfs(node):
            if node is None:
                return 0
            
            gain_on_left = max(dfs(node.left), 0)
            gain_on_right = max(dfs(node.right), 0)
            
            current_path_sum = node.val + gain_on_left + gain_on_right
            
            self.max_path_sum = max(current_path_sum, self.max_path_sum)
            
            return node.val + max(gain_on_left, gain_on_right)
            
        dfs(root)
        return self.max_path_sum
