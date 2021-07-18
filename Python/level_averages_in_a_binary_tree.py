from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

"""
bfs since we are trying to perform a calculation on each level of the binary tree

# check if root is None
# use a queue to store nodes at each level one level at a time
# keep track of a running sum and append the average into result
"""

def find_level_averages(root):
  result = []
  if root is None:
    return result

  queue = deque()
  queue.append(root)

  while queue:
    curr_level_length = len(queue)
    level_sum = 0

    for _ in range(curr_level_length):
      curr_node = queue.popleft()
      level_sum += curr_node.val

      if curr_node.left is not None:
        queue.append(curr_node.left)
      if curr_node.right is not None:
        queue.append(curr_node.right)

    result.append(level_sum / curr_level_length)

  return result

# O(N) time complexity, where N is the number of nodes in the given binary tree, since we visit each node of the binary tree once.
# O(N) space complexity since in the worst case the queue we use will store N/2 nodes which occurs at the bottom level. N/2 is asymptotically N.
