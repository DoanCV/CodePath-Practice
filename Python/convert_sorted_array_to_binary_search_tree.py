# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        """
        if not balanced we can just insert to the right, making it a linked list
        
        
        however we need it to be balanced
        based on the example below, it seems like the middle element is always the root and then the middle of each half is the left and right children of the root
            this repeats until we visited everything in nums
        we can use recursion to create nodes
        
        ex. nums = [1,2,3,4,5,6,7]
                     4
                   /   \
                  2     6
                 / \   / \
                1   3 5   7
        """
        return self.ArrayToBST(nums, 0, len(nums) - 1)
    
    def ArrayToBST(self, nums, start, end):
        # if we reach the ends of the given array, we are done
        if start > end:
            return
        
        # get the middle index
            # we need // to deal with even length arrays
        mid = start + (end - start) // 2
        
        # create a new node
        root = TreeNode(nums[mid])
        
        # build left and right children
        root.left = self.ArrayToBST(nums, start, mid - 1)
        root.right = self.ArrayToBST(nums, mid + 1, end)
        
        return root
        
# O(N) time complexity, where N is the length of the array, since we visit each index once.
# O(N) space complexity since the number of elements in our tree is equal to the number of elements in the given array.
