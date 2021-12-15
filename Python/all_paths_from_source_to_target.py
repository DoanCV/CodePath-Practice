"""
We know there is a topological ordering we just want all of them

the input is a graph where the index is the node and the values are the nodes that the index node is directed towards

we can use DFS recursivcely to explore each path
    for each node we visit we can store the path so far then append it to a result which is a list of lists containing valid paths
    
we can also use DFS iteratively with a stack
    convert the given graph to an adjacency list
    add the 0th vertex to the stack with its path so far
    while the stack is not empty we do exactly the same thing as the recursive except we add to the stack instead of recursing with the helper function
"""

class Solution:
    def allPathsSourceTarget(graph):
        
      def dfs_helper(vertex, path):
        # source is vertex 0 and target is node n-1 so if we get to n-1 then we have a path
        if len(graph) - 1 == vertex:
          result.append(path)
        else:
          # recurse through every neighbor and build the path with each neighbor
          for node in graph[vertex]:
            dfs_helper(node, path + [node])
      
      result = []
      dfs_helper(0, [0])
      return result
        
        
