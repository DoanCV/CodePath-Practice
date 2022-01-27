# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
U
we are given the root of the binary tree with n nodes where each node has node.val coins
    the tree hads n coins total

in one move we may choose an adjacent node and move one coin from one node to another
    parent to child
    child to parent
    
return the minimum number of moces to make every node have exactly one coin

M/P
Post order DFS

return the number of coins given to the parent
    null node cant have coins and cant move coins so we return 0
    
since a node can only have 1 coin
    everything else must be moved somewhere else
    each coin not part of the value (node.val - 1) will contribute a step when going back up to the parent

"""

class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        
        self.moves = 0
        
        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            self.moves += abs(left) + abs(right) 
            
            return node.val - 1 + left + right
        
        dfs(root)
        return self.moves
