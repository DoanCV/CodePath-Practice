"""
Given a binary tree and a number ‘S’, find all paths in the tree such that the sum of all the node values of each path equals ‘S’. 
Please note that the paths can start or end at any node but all paths must follow direction from parent to child (top to bottom).
"""

class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def count_paths(root, S):
  """
  DFS recursion
  We have to keep track of the path we are on so we can check if there is a full or partial path length that is valid
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

  # backtrack to process other paths in the recursive call stack
  curr_path.pop()

  return valid_paths

# O(N) time complexity, where N is the number of nodes in the given binary tree, since we visit each node once.
# O(N) space complexity. We are using a curr_path array which in the worst case will hold the entire tree since each node would have only one child like a linkedlist. There is also our recursive call stack which would be the same size.
