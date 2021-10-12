# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.push_to_left(root)
    
    def push_to_left(self, node):
        while node is not None:
            self.stack.append(node)
            node = node.left
    
    def next(self) -> int:
        temp = self.stack.pop()
        self.push_to_left(temp.right)
        return temp.val

    def hasNext(self) -> bool:
        return self.stack


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
