"""
Largest BST Subtree

Find the size of the largest BST 
  Thing is the given tree itself may not be a BST
    we need to check if a subtree is a BST
    then if it is we get the size
  otherwise we check if the children are BSTs
    if they are get the size and so open

the BST check is recursive in nature
the size calculation is also recursive in nature

O(N^2) time complexity where N is the number of nodes in the given binary search tree. This is because in the worst case we will have to first scan the tree then every subtree.
"""
class Node:
  def __init__(self, val, left = None, right = None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def largestBST(self, root):
    if root is None:
      return 0

    # check if current node is a BST, if so return its size
    if self.isBST(root, float("-inf"), float("inf")):
      return self.BSTsize(root)

    # else we need to check the children by calling this function again
    return max(self.largestBST(root.left), self.largestBST(root.right))

  def isBST(self, node, range_min, range_max):
    if node is None:
      return True

    if node.val <= range_min or node.val >= range_max:
      return False 

    return self.isBST(node.left, range_min, node.val - 1) and self.isBST(node.right, node.val + 1, range_max)
  
  def BSTsize(self, node):

    if node is None:
      return 0

    return 1 + self.BSTsize(node.left) + self.BSTsize(node.right)


"""
We can solve in linear time.

If we traverse the tree in bottom-up manner, then we can pass information about subtrees to the parent. 

The passed information can be used by the parent to do BST test (for parent node) only in constant time (or O(1) time). A left subtree need to tell the parent whether it is BST or not and also needs to pass maximum value in it. So that we can compare the maximum value with the parent’s data to check the BST property. Similarly, the right subtree need to pass the minimum value up the tree. The subtrees need to pass the following information up the tree for the finding the largest BST. 
"""
