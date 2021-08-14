# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        
        preorder:
            visit
            left
            right
            
        inorder:
            left
            visit
            right
        
        for in order everything in the left subtree is to the left of the root
        we know every node is unique so we can find the parent of each subtree since we know in the other traversal what is to the left and right
        
        preorder = [3,9,20,15,7]
        inorder = [9,3,15,20,7]
        [3,9,20,null,null,15,7]
        
        
        preorder we see 3
          before 3 of inorder is the left subtree
        9 is the parent of the left subtree
        in preorder we skip until something in right subtree and get 20
          20 is parent of right subtree
            and so on...
            
        the problem is how long we take to get to the middle or the parent of each subtree
            we repeat this process for each subtree which is O(N^2)
            instead we can use hashmap, mape the {value at a given index: the index itself}
        
        the idea is to quickly find the "middle" index to split our inorder into two subtrees since we immediately see it in preorder
        then we build each subtree in the same manner by recursively splitting our inorder
        
        [9,                3,                15,     20,    7]
        
        """
