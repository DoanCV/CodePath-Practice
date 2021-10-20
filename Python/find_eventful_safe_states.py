"""
We are looking for nodes that are not part of the cycle


Graph coloring 
    0 unvisited
    1 visiting 
    2 visited
    
    
DFS
    We can traverse on each node and DFS into each node that it directs into
    Keep track of the visited nodes

"""

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        colors = [0 for i in range(len(graph))]
        
        def color(index):
            
            if colors[index] == 1:
                return True
            
            if colors[index] == 2:
                return False
            
            colors[index] = 1
            
            for node in graph[index]:
                if color(node):
                    return True
                
            colors[index] = 2
            return False

        
        for i in range(len(graph)):
            color(i)
        
        return [i for i in range(len(graph)) if colors[i] == 2]
