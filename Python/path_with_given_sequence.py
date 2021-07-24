class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

"""
DFS by recursion
keep track of the current path index (depth)
we will compare the current node value
once we are at a leaf node compare the given sequence and the final pathindex value
  if they match return True
return False after the search finishes
"""

def find_path(root, sequence):
  # if the tree is empty we need to check if the sequence is also empty becuase an empty tree and sequence should return True
  if not root:
    return len(sequence) == 0

  return dfs(root, 0, sequence)

def dfs(current_node, depth, sequence):
  # if we are at a null node then there is nothing to compare
  if current_node is None:
    return False
  
  # if the depth or "length" of our path is greater than the length of the given sequence, this path is not valid
  # if the current index of the sequence is not equal to the node value at the current depth, we do not have a match
  if sequence[depth] != current_node.val or depth >= len(sequence):
    return False

  # if we are at a leaf node and at the end of the sequence then we have a valid path
  if current_node.left is None and current_node.right is None and depth == len(sequence) - 1:
    return True
  
  # recurse through the left and right subtrees
  return dfs(current_node.left, depth + 1, sequence) or dfs(current_node.right, depth + 1, sequence)

# O(N) time complexity, where N is the number of nodes in the given binary tree, since in the worst case we visit each node once
# O(N) space complexity since we have a recursive call stack
