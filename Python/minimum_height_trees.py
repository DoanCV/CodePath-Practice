"""
U
We are given the edges of the graph
    the graph is guaranteed to be a tree 

the minimum height tree is just a choice for the root that minimizes the height of the tree compared to its other possible combinations
    return a list of these nodes, any order is fine
 
edge case:
    one node, no edges 
        return 0

M
there are at most 2 MHTs
    if there are 3 then the middle node should be the only MHT making it 1

the middle points of the longest paths always gives the answer so if we can start from the outside, the leaf nodes, then we can find the root labels

we want as many nodes close to the root as possible
    this way the ones that are far out are the minimum heights

the solution should look very similar to topological sort with BFS since we are removing leaf nodes just like removing the indegrees

"""
from collections import defaultdict
from collections import deque
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        # build the graph from the given list of edges
        # neighbors = {vertex: [adjecent verticies]}
        # indegrees = {vertex: degree}
        neighbors = defaultdict(list)
        indegrees = defaultdict(int)
        for u, v in edges:
            neighbors[u].append(v)
            neighbors[v].append(u)
            indegrees[u] += 1
            indegrees[v] += 1
        
        
        # find the leaves
            # leaf nodes have degree 1
        # add them to a queue
        q = deque()
        for k in neighbors:
            if indegrees[k] == 1:
                q.append(k)
                
        # BFS
        # remove unnecessary (leaf) layers
        # discard the previous layer you peel off with each iteration so that we only maintain the last layer 

        visited = set()
        while q:
            # discard older layers by resetting back to empty list 
            layer = [] 
            layerSize = len(q)
            for i in range(layerSize):
                node = q.popleft()
                visited.add(node)
                layer.append(node)
                for nei in neighbors[node]:
                    if nei not in visited:
                        indegrees[nei] -= 1 # cut tie
                        if indegrees[nei] == 1: # new leaf yet?
                            q.append(nei)
        return layer
