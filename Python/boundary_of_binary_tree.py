"""
the boundary of a binary tree is the left boundary + leaf nodes + right boundary in an anticlockwise manner

the left boundary of a binary tree is the path from the root to the left most node
the right boundary of a binary tree is the path from the root to the right most node

return the boundary of the binary tree

ex.
    ____1_____
   /          \
  2            3
 / \          / 
4   5        6   
   / \      / \
  7   8    9  10  

ans = [1,2,4,7,8,9,10,6,3]


we can split the boundary into three parts
  left, leaf and right
  we of course have to remember to not have repeating nodes

left:
  starting from the root
  if we do not have a leaf node add it to the boundary
  go as far left as we can, otherwise we have to go right

right:
  just like left but it is backwards so we have to reverse the results since we start at the root

leaf:
  pre order
  add only if root
"""

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

class Solution:

  def boundary_of_binary_tree(self, root):

    if not root:
      return []

    boundary = [root.val]

    # left boundary
    curr = root.left
    while curr:
      
      # if not leaf node
      if curr.left or curr.right:
        boundary.append(curr.val)
      
      if curr.left:
        curr = curr.left
      else:
        curr = curr.right

    # leaf
    def add_leaves(node):

      if (not node.left) and (not node.right):
        boundary.append(node.val)
        return
      
      if node.left:
        add_leaves(node.left)

      if node.right:
        add_leaves(node.right)

    # right boundary
    curr = root.right
    stack = []
    while curr:

      if curr.left or curr.right:
        stack.append(curr.val)
      
      if curr.left:
        curr = curr.left
      else:
        curr = curr.right
    
    for _ in range(len(stack)):
      boundary.append(stack.pop())

    return boundary
