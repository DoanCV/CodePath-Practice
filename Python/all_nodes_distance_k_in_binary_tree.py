# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
U
given a binary tree, a target node and a distance k, return na array of all the values of all the node that are k away from the target node

M
dfs graph

P
we are given a tree which is a DAG
    build an adjacency list of the tree to later traverse like a graph, the adjacency list will map to its neighbors
    we use dfs in both cases
    
"""
from collections import defaultdict
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        def build_adjacency_list(node):
            if node.left:
                adjacency_list[node].append(node.left)
                adjacency_list[node.left].append(node)
                build_adjacency_list(node.left)
            
            if node.right:
                adjacency_list[node].append(node.right)
                adjacency_list[node.right].append(node)
                build_adjacency_list(node.right)
            
        
        def dfs(node, distance):
            
            if distance < k:
                visited.add(node)
                for neighbor in adjacency_list[node]:
                    if neighbor not in visited:
                        dfs(neighbor, distance + 1)
            
            else:
                result.append(node.val)
            
            
        adjacency_list = defaultdict(list)
        build_adjacency_list(root)
        
        result = []
        visited = set()
        dfs(target, 0)
        
        return result
