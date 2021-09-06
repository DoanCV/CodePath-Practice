from collections import deque

def topological_sort(vertices, edges):
  sortedOrder = []
  
  if vertices <= 0:
    return sortedOrder

  # store the graphs in adjacency lists
      # map = {parent vertex : list of children verticies} 
  graph = {i : [] for i in range(vertices)}
  
  # to find the sources we will count the indegrees for each vertex
      # a vertex with an indegree count of 0 is a source
  inDegree = {i : 0 for i in range(vertices)}
  
  # build the graph
  for edge in edges:
    parent, child = edge[0], edge[1]

    # add the child to its parent's list of children
    graph[parent].append(child)

    # increment the child's inDegree count
    inDegree[child] += 1

  # get all sources, verticies with inDegree count of 0
  # use a queue since we will go degree by degree starting from the source
  sources = deque()
  for key, value in inDegree.items():
    if value == 0:
        sources.append(key)
  
  # add the source to the sortedOrder output
      # subtract 1 from the inDegree count of the children
      # if it becomes a source, push it to the queue
  while sources:
    vertex = sources.popleft()
    sortedOrder.append(vertex)

    for child in graph[vertex]:
      inDegree[child] -= 1
      if inDegree[child] == 0:
        sources.append(child)
  
  # if the queue is not empty, then the graph is not a DAG
  if len(sortedOrder) != vertices:
    return []

  return sortedOrder


def main():
  print("Topological sort: " +
        str(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]])))
  print("Topological sort: " +
        str(topological_sort(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]])))
  print("Topological sort: " +
        str(topological_sort(7, [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]])))


main()

# O(V + E) time complexity where V is the number of vertices in the graph and E is the number of edges in the given graph. Traversing the graph with a breadth first search means that we only visit each vertex once. We also add each edge once. We lookup keys in our hashmap implementation of adjacency list and inDegree frequency map but that is all constant time operations.
# O(V + E) space complexity since we are storing the edges and verticies in an adjacency list.
