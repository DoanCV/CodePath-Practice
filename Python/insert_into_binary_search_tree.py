# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            root = TreeNode(val)
            return root
        
        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        elif root.val < val:
            root.right = self.insertIntoBST(root.right, val)
            
        return root
    
# O(N) time complexity, where N is the number of nodes in the given binary tree, since in the worst case we have a BST where each node has only child node and we have to go all the way to the end.
# O(N) space complexity since we have out recursive call stack and in the worst case we reach the lowest depth.
