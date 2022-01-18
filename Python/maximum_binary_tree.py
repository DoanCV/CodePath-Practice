# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
DFS iterative

Scan the elements of the given array from left to right
    build the tree one node at a time
    make sure the elements of the stack are in decreasing order (to connect the right children)
    for each number, we keep pop the stack until empty or a bigger number
        the bigger number (if exist, it will be still in stack) is current number's root
        the last popped number (if exist) is current number's left child
    then we push current number into the stack

the greatest element will eventually be the first element in the stack

ex. [3,2,1,6,0,5]

num = 3
add to stack
[3]

num = 2
3 is parent of 2
add to stack
[3,2]

num = 1
2 is parent of 1
add to stack
[3,2,1]

num = 6
6 will eventually be the parent of 3
add to stack
[6]

num = 0
6 is parent of 0
add to stack
[6,0]

num = 5
5 is parent of 0
6 is parent of 5
add to stack
[6,5]

return 6 since that is root
"""
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        stack = []
        for num in nums:
            node = TreeNode(num)
            
            while stack and num > stack[-1].val:
                node.left = stack.pop()
            
            if stack:
                stack[-1].right = node
            
            stack.append(node)
            
        return stack[0]
