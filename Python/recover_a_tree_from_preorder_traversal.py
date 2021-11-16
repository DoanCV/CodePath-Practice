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

Nodes with one child means that the child is a left child




DFS iterative

Use a hashmap to store the level and the nodes at each level

First we scan the input for two cases:
    levels based on the number of dashes or the digits
    note that apart from the root of the tree, all nodes are preceeded by dashes
    
Once we finish scanning a digit we know we have a node so we can add to the tree

potential logic challenge:
    each level may have many nodes
    we will reset it each time we find the same level again since by the time we find the next level the current one would already have been completely built out


O(N) time complexity where N is the length of the given string since we solve in one pass. We iterate through each character of the string and we revisit parent nodes by taking advantage of constant time lookups with our hashmap.
O(numNodes) space complexity since we use a hashmap that relates the depth to the node at that depth that we will use to build the tree. The numNodes is the worst case depth of the binary tree and that will add keys to our hashmap.
"""
from collections import defaultdict
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        
        hashmap = defaultdict()
        
        i = 0
        while i < len(traversal):
            curr_level = 0
            curr_node_val = 0
            
            # we found dashes
            while i < len(traversal) and traversal[i] == "-":
                curr_level += 1
                i += 1
            
            # we found digits
                # do not change to int in the while statement, only do that inside the loop, since "-" is not in between "0" - "9" and we can use this fact
            while i < len(traversal) and traversal[i] >= "0" and traversal[i] <= "9": 
                curr_node_val = curr_node_val * 10 + int(traversal[i])
                i += 1
            
            # create the node, add the current node to the corresponding level in the hashamp and add to tree using the parent node
            curr_node = TreeNode(curr_node_val)
            hashmap[curr_level] = curr_node
            
            if curr_level > 0:
                parent_node = hashmap[curr_level - 1]
                
                # default current node to child of parent otherwise make that the right child
                if parent_node.left is None:
                    parent_node.left = curr_node
                else:
                    parent_node.right = curr_node 
        
        return hashmap[0]
