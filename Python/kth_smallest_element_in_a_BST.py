# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
U
given the root of a binary search tree
    return the kth smallest value (1 indexed)

M/P
DFS in order traversal (left child, parent, right child)
    iteratively with stack
    we know tree is BST so we go left as far as we can
    then for each element in the stack we pop and decrement k until we hit 0
        check the right subtree of the current parent

E
O(N) time complexity where N is the number of nodes in the given tree. We visit each node once in the worst case which can happen when the tree is left heavy or k is equal to N.
O(N) space complexity since we are using a stack that is worst case the depth of the tree.
"""
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        stack = []
        
        while root or stack:
            
            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            k -= 1
            
            if k == 0:
                return root.val
            
            root = root.right
