"""
Given a binary tree where each node can only have a digit (0-9) value, each root-to-leaf path will represent a number. 
Find the total sum of all the numbers represented by all paths.
"""

class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def find_sum_of_path_numbers(root):
  """
  DFS
  keep track of the current path, convert the value at the given node to string and concatenate the entire path
    add the full integer path value to a cumulative sum
    return this sum
  """
  # if the given binary tree does not have any nodes, return 0
  if root is None:
    return 0

  # start the recursive DFS, keep track of the cumulative sum, path values, the current node
  all_path_sum = []
  dfs(root, "", all_path_sum)

  result = 0
  for i in range(len(all_path_sum)):
    result += all_path_sum[i]

  return result

def dfs(current_node, path_sum, all_path_sum):

  # if not at a node, return nothing
  if current_node is None:
    return
  
  # add the integer value of the node to the path_sum
  current_value = str(current_node.val)
  path_sum += current_value

  # if at a leaf node, add the path_sum to all_path_sum
  if current_node.left is None and current_node.right is None:
    path_sum_int = int(path_sum)
    all_path_sum.append(path_sum_int)
  else:
    # recurse to the left substree and right subtree
    dfs(current_node.left, path_sum, all_path_sum)
    dfs(current_node.right, path_sum, all_path_sum)
    
  # backtrack when we are at the top of the recursive call stack
  path_sum.rstrip()
  
# O(N) time complexity, where N is the number of nodes in the given binary tree, since we have to visit each node once.
# O(N) space complexity since we have a recursive call stack. In the worst case each node has only one child node like a linkedlist.




"""
A cleaner solution:
We have used a string to concatentate the digits of out path value and an array since all_path_sum would not return properly.
  Instead, path_sum = path_sum * 10 + current_node.val

def find_sum_of_path_numbers(root): 
  return dfs(root, 0)

def dfs(current_node, path_sum):
  if current_node is None:
    return 0
  
  path_sum = path_sum * 10 + current_node.val
  
  if current_node.left is None and current_node.right is None:
    return path_sum
  
  return dfs(current_node.left, path_sum) + dfs(current_node.right, path_sum)
"""
