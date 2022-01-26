# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
U
given the root of a binary tree and a target sum
    return the number of paths where the sum of the values along the path equals target sum

M
cache
    map pathsum (from root to current node) to its encountered frequency

if we have a path sum equal to the target at the current node then it would be current sum - target
    if this is the case then we add the frequency to the counter
"""
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        
        self.path_count = 0
        self.cache = {}
        
        self.dfs(root, targetSum, 0)
        
        return self.path_count
    
    def dfs(self, curr_node, target_sum, current_path_sum):
        # do nothing if null node
        if not curr_node:
            return
        
        # increment path counter if the current path sum is equal to the target
        current_path_sum += curr_node.val
        if current_path_sum == target_sum:
            self.path_count += 1
        
        # if current path sum - target sum exists in the cache then we found a path that adds up to the target
        # we are taking advantage of the complement
        # current_path_sum - scrap_path_sum = target_sum
        scrap_path_sum = current_path_sum - target_sum
        if scrap_path_sum in self.cache:
            self.path_count += self.cache[scrap_path_sum]
        
        # account for the encounter
        if current_path_sum not in self.cache:
            self.cache[current_path_sum] = 0
        self.cache[current_path_sum] += 1
        
        # recurse to the left and right subtrees
        self.dfs(curr_node.left, target_sum, current_path_sum)
        self.dfs(curr_node.right, target_sum, current_path_sum)
        
        # the current path sum is no longer available since we moved up
        self.cache[current_path_sum] -= 1
