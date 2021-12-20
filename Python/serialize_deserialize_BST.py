# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        
        values = []
        
        # preorder traversal
        def dfs(node):
            if node:
                values.append(str(node.val))
                dfs(node.left)
                dfs(node.right)
                
        dfs(root)    
        
        return " ".join(values)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        
        queue = deque(int(val) for val in data.split())
        
        def build(lower_bound, upper_bound):
            
            if queue and queue[0] < upper_bound and queue[0] > lower_bound:
                val = queue.popleft()
                node = TreeNode(val)
                node.left = build(lower_bound, val)
                node.right = build(val, upper_bound)
                return node
        
        return build(float("-inf"), float("inf"))
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans


# Serialize
# O(N) time complexity where N is the size of the binary search tree. We visit each node once in our preorder depth first search
# O(N) space complexity since we have a string with all the values of the nodes.

# Deserialize
# O(N) time complexity where N is the length of the serialized string. We visit each value once.
# O(N) space complexity since we use a queue to store all the values and we have a TreeNode for each value.
