from __future__ import print_function
from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right, self.next = None, None, None

  # level order traversal using 'next' pointer
  def print_level_order(self):
    nextLevelRoot = self
    while nextLevelRoot:
      current = nextLevelRoot
      nextLevelRoot = None
      while current:
        print(str(current.val) + " ", end='')
        if not nextLevelRoot:
          if current.left:
            nextLevelRoot = current.left
          elif current.right:
            nextLevelRoot = current.right
        current = current.next
      print()

"""
bfs since we can keep track of nodes on a level with a queue

keep track of the previous node in the current level to use .next to point it to the next node
if there is no next node in the current level, point to None
"""

def connect_level_order_siblings(root):
  # check if the tree is empty
  if root is None:
    return None
  # create queue and append root
  queue = deque()
  queue.append(root)
  # while the queue is not empty
  while queue:
    # get the length of the current level
    current_level_length = len(queue)
    # previous node is None
    prev = None
    # loop through the length of the level
    for i in range(current_level_length):
      # popleft for current node
      current_node = queue.popleft()
      # check children to add to the queue
      if current_node.left is not None:
        queue.append(current_node.left)
      if current_node.right is not None:
        queue.append(current_node.right)
      # if previous is not None .next is current node
      if prev is not None:
        prev.next = current_node
      # if at the end of the for loop current.next is None
      if i == current_level_length - 1:
        current_node.next = None
      # save current node as previous
      prev = current_node
  return
