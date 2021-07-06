"""
breadth first search since we are traversing by level
logic:
if root is None
  return empty result

# first level is the root
append the root to the queue (i will use a deque)

# go through each level, the queue will be empty when we finished all levels
while the queue is not empty:
  # go through a level
  find the length of the queue since that holds the current level
  loop through the level length (length of queue)
    pop queue to get the current node (popleft deque)
    add the current node to the current level

    if the left child of current node is not None
      append to queue
    if the right child of current node is not None
      append to queue
  
  # add the level to the results

# return the result
"""
def traverse(root):
  result = []
  if root is None:
    return result
  
  queue = deque()
  queue.append(root)
  
  while queue is not None:
    level_length = len(queue)
    curr_level = []
    
    for _ in range(level_length):
      curr_node = queue.popleft()
      curr_level.append(curr_node.val)

      if curr_node.left is not None:
        queue.append(curr_node.left)
      if curr_node.right is not None:
        queue.append(curr_node.right)
    
    result.append(curr_level)
  return result
