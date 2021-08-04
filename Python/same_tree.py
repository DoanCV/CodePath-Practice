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
            
            # we already check if both nodes are not empty, now we check if only one is empty and if that is the case the trees are not the same, otherwise both are indeed empty and are the same
            elif nodeP or nodeQ:
                return False
        
        return True

# O(N) time complexity, where N is the number of nodes in the given binary tree, since we have to check all of the nodes anyways.
# O(N) space complexity, for both solutions, since for the dfs recursion we have recursive call stack and for the bfs iterative in the worst case our queue will be size N/2 at the highest depth.
