class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def has_path(root, sum):
  """
  DFS
  Using recursion we send the left child and the right child of the current node
  With each call we subtract the value at the current node from the sum to feed into the call
  If we are at a leaf node and the value we fed in is equal to the value of the leaf node then we have found a path
  """
  if root is None:
    return False

  if (root.left is None and root.right is None) and sum == root.val:
    return True
  
  return has_path(root.left, sum - root.val) or has_path(root.right, sum - root.val)
