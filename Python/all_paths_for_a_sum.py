class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def find_paths(root, sum):
  allPaths = []
  recurse(root, sum, [], allPaths)
  return allPaths

def recurse(currentNode, sum, currentPath, allPaths):
  if currentNode is None:
    return 
  
  # add the current node to the path
  currentPath.append(currentNode.val)
  
  # Check for leaf node and if the value of the node 
  if currentNode.val == sum and currentNode.left is None and currentNode.right is None:
    allPaths.append(list(currentPath))
  else:
    # traverse the left subtree
    recurse(currentNode.left, sum - currentNode.val, currentPath, allPaths)
    # traverse the right subtree
    recurse(currentNode.right, sum - currentNode.val, currentPath, allPaths)
  
  # backtrack 
  currentPath.pop()

# O(N) time complexity, where N is the number of nodes in the given binary tree, since we visit each node once.
# O(N) space complexity since in the worst case each node has only one child like a linkedlist.
