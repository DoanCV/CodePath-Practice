# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        """
        Reminds me of validate binary tree
        
        iterative dfs with a stack
        
        we check the current node value
            if it is in range add it to the total
        
        go left and right
        """
        total = 0
        stack = [(root, low, high)]
        
        while stack:
            curr_node, low, high = stack.pop()
            
            if curr_node is None:
                continue
        
            if curr_node.val >= low and curr_node.val <= high:
                total += curr_node.val
            
            stack.append((curr_node.left, low, high))
            stack.append((curr_node.right, low, high))
        
        return total
      
# O(N) time complexity, where N is the number of nodes in the given binary tree, since we visit each node once
# O(N) space complexity since in the worst case we store the maximum number of nodes at a level which is proportional to N.

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        """
        Lets try recursive dfs
        
        if we are at a leaf node or the tree is empty, the node will contribute 0 to the sum
        
        we will recurse left if the current value is too large since we need a smaller value to add to the total sum
        we will recurse right if the current value is too small since we need a large value to add to the total sum
        
        we will recurse both left and right if the current value is in the range
        """
        
        if root is None:
            return 0
        else:
            if root.val < low:
                total = self.rangeSumBST(root.right, low, high)
            elif root.val > high:
                total = self.rangeSumBST(root.left, low, high)
            else:
                total = root.val + self.rangeSumBST(root.right, low, high) + self.rangeSumBST(root.left, low, high)
        
        return total

# O(N) time complexity since we visit each node once
# O(N) space complexity for the recursive call stack but we do not explicitly use extra data structures.
