from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

"""
bfs since we are doing level traversal

we can account for the zigzag by keeping track of the level and changing the direction in which we append to the queue of nodes
"""

def traverse(root):
  result = []
  if root is None:
    return result
  
  queue = deque()
  queue.append(root)

  direction_left_to_right = True
  while queue:

    current_level_length = len(queue)
    current_level = deque()

    for _ in range(current_level_length):
      current_node = queue.popleft()
      
      if direction_left_to_right:
        current_level.append(current_node.val)
      else:
        current_level.appendleft(current_node.val)
    
      if current_node.left is not None:
        queue.append(current_node.left)
      if current_node.right is not None:
        queue.append(current_node.right)

    result.append(list(current_level))
    direction_left_to_right = not direction_left_to_right
  return result

# O(N) time complexity, where N is the number of nodes in the given binary tree, since we visit each node of the tree once.
# O(N) space complexity since in the worst case the most nodes we have in the queue called queue is N/2, which is at the bottom level. N/2 is asymptotically N.
