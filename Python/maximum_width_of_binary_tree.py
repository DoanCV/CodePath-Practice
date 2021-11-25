# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
We are given a nonempty binary tree and we need to find the maximum width
    a width is the length between the end nodes of a level
    keep in mind the level may not be full so we cant simply take the length of our queue when we use BFS
        consider the case where we have two nodes in a level, doesnt really matter where unless they are next to each other
            we cannot say that the width is 2 since one node can be all the way on the right of the tree and the other on the left most side of the tree
    this means we need to store more information in our queue

We can keep track of the node number which is essentially what we would get from a level order traversal regardless if a node exists or not
    this node number can be mapped between levels

for example, the given tree would look like the following

                    1 
                 /     \
                3       2
              /   \      \
             5     3      9

top down left to right view
node: [node number, level]
1: [1,1]
3: [2,2]
2: [3,2]
5: [4,3]
3: [5,3]
9: [7,3]


to get from level to level during out BFS we have access to the children so how do we map node number from one level to the next
    the left child is 2*node_number 
    the right child is 2*node_number + 1

the width is the difference between the right_node_number - left_node_number + 1

O(N) time complexity where N is the number of nodes in the given tree since we visit each node once.
O(N) space complexity since we use a queue to store nodes to visit level by level.
"""

from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_width = 0
        
        start_node_number = 1
        start_level = 1
        
        queue = deque()
        queue.append([start_node_number, start_level, root])
        
        while queue:
            curr_node_number, curr_level, curr_node = queue.popleft()
            
            # we need to change levels to have the correct calculation, marking the start of a level
            if curr_level > start_level:
                start_level = curr_level
                start_node_number = curr_node_number
                
            max_width = max(max_width, curr_node_number - start_node_number + 1)
            
            if curr_node.left:
                queue.append([curr_node_number * 2, curr_level + 1, curr_node.left])
            
            if curr_node.right:
                queue.append([curr_node_number * 2 + 1, curr_level + 1, curr_node.right])

        return max_width
