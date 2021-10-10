# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
given: root
return: vertical order traversal

vertical and horizontal is defined with coordinates
root is (0,0)

left child of root is (1,-1)
    right child of left child of root is (2,0)
    left child of left child of root is (2,-2)
right child of root is (1,1)
    left child of right child of root is (2,0)
    right child of right child of root is (2,2)

picture:

               8 (0,0)
            /           \
  (1,-1)   9           11 (1,1)
          / \           /   \
  (2,-2) 1   8 (2,0) 3(2,0) 4(2,2)

edge case: empty tree, just return an empty list


M/P
we know what happens to the coordinates when we go left and right from a node

the horizontal distance from the root, ie 0, changes when we go left and right so essentially the columns

we can keep track of the columns and the nodes in the same column in a hashmap 
    within each column we read top down
    {column: []}
        inside each list
        (level, value of node)
    
build the hashmap with preorder traversal

then go through the keys in ascending order and append the values to output then return the output

"""
from collections import defaultdict
from heapq import *

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        coordinates = defaultdict(list)
        
        def dfs(node, horizontal_pos, vertical_pos):
            
            if node is None:
                return
            
            coordinates[horizontal_pos].append( (vertical_pos, node.val) )
            
            if node.left:
                dfs(node.left, horizontal_pos - 1, vertical_pos + 1)
            
            if node.right:
                dfs(node.right, horizontal_pos + 1, vertical_pos + 1)
                
        dfs(root, 0, 0)
    
        output = []
        min_heap = []
        
        # sort the keys and the nodes in the lists on the vertical position
        for column, nodes in coordinates.items():
            
            # sort on vertical, if there is a tie then sort on value
            nodes.sort(key = lambda x: (x[0], x[1]))
            heappush( min_heap, (column, nodes) )
        
        while min_heap:
            output.append([value for _, value in heappop(min_heap)[1]])
        
        return output
