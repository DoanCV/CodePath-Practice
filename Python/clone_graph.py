"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

"""
Clone a graph using the given Node class.
    We can have an empty graph which would return an empty graph

DFS/BFS Iterative

use a stack/queue, if i use pop or popleft in this case it doesnt matter
have a visited set
start with the given node

pop from the stack
go through all the neighbors of the current node
    if the current neighbor is not in the visited set
        add the current neighbor to the stack
        create a copy and add to visited set
    add the copy of the neighbor to the copy of the current node

O(N) time complexity where N is the number of nodes in the given graph since we visit each node once.
O(N) space complexity since we keep a visited map and a stack. The visited map has N keys and the stack is worst case the depth of the graph starting from the given node.
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None
        
        stack = deque()
        stack.append(node)
        visited = {node: Node(node.val)}
        
        while stack:
            curr_node = stack.pop()
            
            for neighbor in curr_node.neighbors:
                if neighbor not in visited:
                    stack.append(neighbor)
                    visited[neighbor] = Node(neighbor.val)
                visited[curr_node].neighbors.append(visited[neighbor])
        
        return visited[node]
