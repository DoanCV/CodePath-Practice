"""
Given a binary tree, 'double' it. For each node, make a duplicate and point the original node to its duplicate.

ex. 
Given:
    2
   / \
  1   3
  
Output:
       2
     /   \
    2     3
   /     /
  1     3
 /
1
"""

"""
DFS 

Post order (recurse left, right, then visit root)
make current node point to copy of left node which will point to the original of the left node
"""
class TreeNode():
  def __init__(self, val, left, right):
    self.val = val
    self.left = left
    self.right = right

def doubleTree(root):
  if root is None:
    return
  
  doubleTree(root.left)
  doubleTree(root.right)
  
  old = root.left
  root.left = TreeNode(root.val)
  root.left.left = old
  
  return root
