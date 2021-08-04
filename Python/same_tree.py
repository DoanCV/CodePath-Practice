from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        """
        # dfs recursion
        if p is not None and q is not None:
            
            if p.val == q.val:
                valueMatch = True
            else:
                valueMatch = False
                
            leftMatch = self.isSameTree(p.left, q.left)
            rightMatch = self.isSameTree(p.right, q.right)
            
            return valueMatch and leftMatch and rightMatch
        
        return p == q
        """
        # BFS
        
        queue = deque()
        queue.append( (p, q) )
        
        while queue:
            
            nodeP, nodeQ = queue.popleft()
            
            if nodeP and nodeQ:
                if nodeP.val != nodeQ.val:
                    return False
                
                queue.append( (nodeP.left, nodeQ.left) )
                queue.append( (nodeP.right, nodeQ.right) )
                
            elif nodeP or nodeQ:
                return False
        
        return True
