class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def count_paths(root, S):
  """
  """
  return dfs(root, S, [])

def dfs(curr_node, S, curr_path):
  if curr_node is None:
    return 0
  
  curr_path.append(curr_node.val)

  valid_paths = 0

  # go backwards in the path until there is a valid sum then increment count
  curr_sum = 0
  for i in range(len(curr_path) - 1, -1, -1):
    curr_sum += curr_path[i]
    if curr_sum == S:
      valid_paths += 1
  
  # recurse left and right subtrees
  valid_paths += dfs(curr_node.left, S, curr_path)
  valid_paths += dfs(curr_node.right, S, curr_path)

  curr_path.pop()

  return valid_paths
