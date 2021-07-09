from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

"""
bfs since we are looking for the minimum depth where we have a leaf node

same idea as tree level traversal but we do not keep track of the nodes at each level, instead we keep track of the depth and return it once we are at the bottom
"""

def find_maximum_depth(root):
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

      if curr_node.left is not None:
        queue.append(curr_node.left)
      if curr_node.right is not None:
        queue.append(curr_node.right)
      
  return depth

# O(N) time complexity, where N is the number of nodes in the given binary tree, since we have to visit every node once.
# O(N) space complexity since in the worst case the bottom level will have N/2 nodes which is asymptotically N.
