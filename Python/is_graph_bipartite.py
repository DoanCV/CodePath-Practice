"""
U
input is the nodes adjacent to the vertex with a default value of its index

We need to split veritices into two groups such that each vertex in one group is not adjacent to each other

M
we can use two flags to determine which of the two groups in the parittion that a vertex will belong to
    we can keep track of the nodes that we visited in a hashmap
    hashmap = {vertex: color}
    colors = 0 or 1
the nodes that are adjacent must be of the opposite color

we can traverse the graph with DFS

P
for each index, ie vertex, in the graph
    set the vertex's flag to 0
    
    call helper function with the current vertex
        if it returns False then the graph is not bipartite
return True since the graph passed the check

helper function
for each adjacent vertex to the one we are currently checking in main
    if the adjacent vertex has already been visited then check if it has the same flag as the one we fed into the helper function
        if it is the graph is not bipartite
    else
        set the flag to the opposite of the current flag
        
        recurse to the next check
    
    return True since adjacent verticies are opposite colors so far

"""

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited_colors = {}
        
        def dfs(position):
            
            for adjacent_vertex in graph[position]:
                
                if adjacent_vertex in visited_colors:
                    if visited_colors[adjacent_vertex] == visited_colors[position]:
                        return False
                
                else:
                    visited_colors[adjacent_vertex] = 1 - visited_colors[position]
                    
                    if not dfs(adjacent_vertex):
                        return False

            return True
        
        
        for vertex in range(len(graph)):
            
            if vertex not in visited_colors:
                
                visited_colors[vertex] = 0
                
                if not dfs(vertex):
                    return False
                
        return True
