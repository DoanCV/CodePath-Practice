"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = self.right = None
"""
"""
Store inorder traversals of both trees in a list then combine them, sort and
then build
oh wait O(M+N) time maybe the above is slower than this?
no need to sort, everything is already in order one pass is enough to combine them
"""
def merge(root1, root2):
    """
    Write your code here
    :type tree1: TreeNode
    :type tree2: TreeNode
    :rtype: TreeNode
    """
    def find_inorder1(node, arr1):
        if node:
            find_inorder1(node.left, arr1)
            arr1.append(node.val)
            find_inorder1(node.right, arr1)
    def find_inorder2(node, arr2):
        if node:
            find inorder1(node.left, arr2)
            arr2.append(node.val)
            find_inorder2(node.right, arr2)
            
    arr1 = []
    arr2 = []
    find_inorder1(root1, arr1)
    find_inorder2(root2, arr2)

    # depending on how we merge these arrays we can get linear time, they are both sorted so we can do this
    merged_array = merge_two_sorted_arrays(arr1, arr2)
    # now build the new binary search tree with a sorted array
    return sorted_array_to_BST(merged_array, 0, len(merged_array) - 1)
      
      
def merge_two_sorted_arrays(arr1, arr2):
      result = []
      left1 = 0
      left2 = 0
      while left1 < len(arr1) and left2 < len(arr2):
          if arr1[left1] < arr2[left2]:
              result.append(arr1[left1])
              left1 += 1
          else:
              result.append(arr2[left2])
              left2 += 1

      # we hit the end of one of them now add the rest
      while left1 < len(arr1):
          result.append(arr1[left1])
          left1 += 1
      while left2 < len(arr2):
          result.append(arr2[left2])
          left2 += 1
      return result
    
    
def sorted_array_to_BST(arr, left, right):
    if left > right:
      return
    
    mid = left + (right - left) // 2
    
    root = TreeNode(arr[mid])
    
    root.left = sorted_array_to_BST(arr, left, mid - 1)
    root.right = sorted_array_to_BST(arr, mid + 1, right)
    
return root
