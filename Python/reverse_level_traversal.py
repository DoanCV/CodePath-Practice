from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

"""
bfs since we are doing level by level traversal
similar to level order traversal starting at the root
  difference is we can just append to the front of the result array (deque since we can use appendleft())
"""

def traverse(root):
  result = deque()
  if root is None:
    return result
  
  level = deque()
  level.append(root)

  while level:
    current_level = []
    curr_level_length = len(level)

    for _ in range(curr_level_length):
      curr_node = level.popleft()
      current_level.append(curr_node.val)

      if curr_node.left is not None:
        level.append(curr_node.left)
      if curr_node.right is not None:
        level.append(curr_node.right)
      
    result.appendleft(current_level)

  return result

# O(N) time complexity, where N is the number of nodes in the binary tree, since we visit each node once.
# O(N) space complexity since in the worst case the lowest level will have N/2 nodes which is the highest possible.
