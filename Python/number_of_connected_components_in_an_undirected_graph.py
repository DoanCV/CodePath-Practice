class Solution:
  def countComponents(self, n, edges):
    
    parent = [i for i in range(n)]
    rank = [1 for _ in range(n)]

    # find root parent
    def find(node):

      res = node

      # stop when the node's parent is itself
      while res != parent[res]:
        parent[res] = parent[parent[res]] # path compression, make grandparent the parent
        res = parent[res]
      
      return res
    
    def union_find(node1, node2):
      parent1, parent2 = find(node1), find(node2) # get root parents

      # same parent node so no union
      if parent1 == parent2:
        return 0 

      # merge and update the rank of the parent
      if rank[parent2] > rank[parent1]:
        parent[parent1] = parent2
        rank[parent2] += 1 
      else:
        parent[parent2] = parent1
        rank[parent1] += 1 

      return 1 # union sucessful

    # if we can merge nodes together then we have fewer groups of connected components since we start with the assumption that all nodes are disjoint until we check.
    components = n
    for node1, node2 in edges:
      components -= union_find(node1, node2)

    return components
