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

  direction_left = True
  while queue is not None:

    current_level_length = len(queue)
    reordered_level = deque()

    for _ in range(current_level_length):
      current_node = queue.popleft()
      
      if direction_left:
        reordered_level.append(current_node.val)
      else:
        reordered_level.appendleft(current_node.val)
    
      if current_node.left is not None:
        queue.append(current_node.left)
      if current_node.right is not None:
        queue.append(current_node.right)

    result.append(list(reordered_level))
    direction_left = not direction_left
  return result
