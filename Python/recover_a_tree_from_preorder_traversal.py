# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
We are given a preorder traversal of a tree (has to be binary based on our TreeNode definition) in the form of a string
    The string has the node valie and dashes, ie "-", which denotes the depth of the node

ex. "1-2--3--4-5--6--7"
node depth number of dashes before it
1 depth 0
2 depth 1
3 depth 2
4 depth 2
5 depth 1
6 depth 2
7 depth 2

With this string recover the tree, ie. build it, and return the root of the tree
    since we use dashes we have to constrain the node values to positives since otherwise the "-" could mean negative value
    also keep in mind that the input is a string so we have to scan for entire node values


DFS recursion with helper function

First we split the input into levels based on the number of dashes
After we split we have a few possibilites
    No splitters, this means our entire string is a node value
    One splitter, ie one sided tree
    Two splitters, ie we have left and right subtree
    
"""
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
      
