"""
Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]

a -> b, edge value = 2.0
b -> a, edge value = 1/2.0 = 0.5

b -> c, edge value = 3.0
c -> b, edge value = 1/3.0

(a/b)*(b/c) = a/c


iterative BFS

build adjacency list, each edge is weighted
{numerator: (denominator, weight), (), ...}
start with 1.0 

start with the numerator of the query
    if the vertex is not in our graph, either the numerator or denomintor return -1.0, check this first
    if numerator == denominator return the current product
    
    keep a visited set
    
    search through each level, ie. list of neighbors, and if we havent visited it yet then add it with the updated product to our queue

if our queue is empty that means we do not have a path for out query so return -1.0


O(E + V) time complexity where E is number of equations and V is number of variables since we build graph by visiting verticies only once. Similarly in our BFS we have visited set so we only visit vertex once.
O(V) space complexity. The memory we are using is the visited set, graph in the form of adjacency list and the queue. The set is at worst the entire graph so all verticies. The hashmap of our graph will also have to store all the verticies as its keys by default. The queue will be the size of our level which can't be more than the number of verticies in our graph.
"""

from collections import defaultdict
from collections import deque
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        graph = self.build_graph(equations, values)
        
        output = []
        for numerator, denominator in queries:
            output.append(self.bfs(numerator, denominator, graph))
        
        return output
    
    def build_graph(self, equations, values):
        graph = defaultdict(list)
        
        for i in range(len(equations)):
            graph[equations[i][0]].append( (equations[i][1], values[i]) )
            graph[equations[i][1]].append( (equations[i][0], 1/values[i]) )
        
        return graph
    
    def bfs(self, numerator, denominator, graph):
        queue = deque()
        queue.append( (numerator, 1.0) )
        visited = set()

        while queue:
            
            curr_vertex, curr_val = queue.popleft()
            
            if curr_vertex not in graph or denominator not in graph:
                return -1.0
            
            elif curr_vertex == denominator:
                return curr_val
                      
            visited.add(curr_vertex)
            
            for neighbor, edge_val in graph[curr_vertex]:
                if neighbor not in visited:
                    queue.append( (neighbor, curr_val * edge_val) )
        
        return -1.0
