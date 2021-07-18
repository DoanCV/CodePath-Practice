# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.cur_sum_ = 0
        def recursion(root):
            if not root:
                return
            if root and root.left and (not root.left.left and not root.left.right):
                self.cur_sum_ += root.left.val
            recursion(root.left) 
            recursion(root.right)
        recursion(root)    
        return self.cur_sum_
