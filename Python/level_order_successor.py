from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

"""
bfs since we can use the queue to find the next node in the level traversal

once the value we just popped from the queue has the same value as the given key we will return the bottom node of the queue since that is next in the level traversal
if the queue is empty then return None
"""

def find_successor(root, key):
  if root is None:
    return None
  
  queue = deque()
  queue.append(root)

  while queue:
    curr_level_length = len(queue)
    for _ in range(curr_level_length):
      curr_node = queue.popleft()

      if curr_node.left is not None:
        queue.append(curr_node.left)
      if curr_node.right is not None:
        queue.append(curr_node.right)

      if curr_node.val == key:
        break

  if queue:
    return queue[0]
  else:
    return None
  
# O(N) time complexity, where N is the number of nodes in the given binary tree, since in the worst case we traverse the entire tree therefore visited every node.
# O(N) space complexity since in the worst case we end up at the bottom level which can have N/2 nodes which occupy our queue.
