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
  
  currentPath.append(list(currentNode))

  if currentNode.val == sum and currentNode.left is None and currentNode.right is None:
    allPaths.append(currentPath)
  else:
    recurse(currentNode.left, sum - currentNode.val, currentPath, allPaths)
    recurse(currentNode.right, sum - currentNode.val, currentPath, allPaths)

  currentpath.pop()
