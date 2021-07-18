from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

"""
bfs since we are looking for the minimum depth where we have a leaf node

same idea as tree level traversal but we do not keep track of the nodes at each level, instead we keep track of the depth and return it once we find a leaf node
"""

def find_minimum_depth(root):
  if root is None:
    return 0

  queue = deque()
  queue.append(root)
  depth = 0
  while queue:
    depth += 1
    curr_level_size = len(queue)

    for _ in range(curr_level_size):
      curr_node = queue.popleft()

      if curr_node.right is None and curr_node.left is None:
        return depth
      
      if curr_node.left is not None:
        queue.append(curr_node.left)
      if curr_node.right is not None:
        queue.append(curr_node.right)
      
  return -1

# O(N) time complexity, where N is the number of nodes in the given binary tree, since in the worst case the first leaf node is at the far right on the second to last level. Regardless, we have to traverse each node once to get there.
# O(N) space complexity since in the worst case we will have to store the bottom level in the queue which is the largest level and have size of N/2.
