"""
We are given an undirected graph, find the shortest path that visites every node. 
We can start and stop at any node. 
We can revisit nodes multiple times and we can reuse edges.
The weight of each edge is 1 



We can use BFS
We initialize our queue to contain N possible paths each starting from nodes [0,N-1]. This is because we can start at any of N possible Nodes.

At each step, we remove element from the queue and see if we have covered all 12 nodes in our bitMask. If we cover all nodes, we return the cost of the path immediately. Since we are using BFS, this is guranteed to be path with the lowest cost.

Otherwise, we get all the neighbors of current node, and for each neighbor, set the Node to visited in bitMask, and then add it back into the queue

deque([(0, 1), (1, 2), (2, 4), (3, 8)])
allVisited = 15

O(N * 2^N) time complexity since there are 2^N possible paths starting from a given node and there are N nodes.
O(N * 2^N) space complexity since our hashamp stores all the possible states.
"""
from collections import deque
from collections import defaultdict
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        nodeCount = len(graph)
        all_visited = (1 << nodeCount) - 1

        queue = deque([(i, 1 << i) for i in range(nodeCount)])
        steps = defaultdict(lambda: nodeCount*nodeCount)
        
        for i in range(nodeCount):
            steps[i, 1 << i] = 0
        
        while queue:

            curr_node, curr_path = queue.popleft()
            curr_steps = steps[curr_node, curr_path]
            
            if curr_path == all_visited:
                return curr_steps
                
            for neighbor in graph[curr_node]:
                neighbor_steps = curr_path | 1 << neighbor # bitwise OR operation to add the neighbor to the path
                
                # never visited before include in path
                if steps[neighbor, neighbor_steps] > curr_steps + 1:
                    steps[neighbor, neighbor_steps] = curr_steps + 1
                    queue.append( (neighbor, neighbor_steps) )
    
