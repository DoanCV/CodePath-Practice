"""
Problem: 
  There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. 
  Each task can have some prerequisite tasks which need to be completed before it can be scheduled. 
  Given the number of tasks and a list of prerequisite pairs, write a method to print all possible ordering of tasks meeting all prerequisites


Topological sort but we return all valid orderings

We will recursively explore options with a helper function
  at any level we may have more than 1 source so we need to branch out and then backtrack 

  at any point when we have processed all the courses then we will print them
    otherwise we know that we are either not done or have a cycle
  
"""

from collections import deque

def print_orders(tasks, prerequisites):
  sorted_order = []
  # case 0: tasks <= 0
  if tasks <= 0:
    return sorted_order

  # initialize adjacency list
  graph = {i : [] for i in range(tasks)}

  # initialize inDegree count
  inDegree = {i : 0 for i in range(tasks)}

  # build the graph
  for edge in prerequisites:
    parent, child = edge[0], edge[1]

    graph[parent].append(child)

    inDegree[child] += 1

  # add first level of sources to a queue
  queue = deque()
  for key, value in inDegree.items():
    if value == 0:
      queue.append(key)

  # recurse with a breadth first search
  print_order_paths(graph, inDegree, queue, sorted_order)

def print_order_paths(graph, inDegree, queue, sorted_order):
  if queue:

    # BFS
    for task in queue:
      sorted_order.append(task)
      copy = deque(queue)
      copy.remove(task)

      # decrement child inDegree count
      for child in graph[task]:
        inDegree[child] -= 1
        if inDegree[child] == 0:
          copy.append(child)

      # continue recursing with a copy of our queue
      print_order_paths(graph, inDegree, copy, sorted_order)

      # backtrack
      sorted_order.remove(task)
      for child in graph[task]:
        inDegree[child] += 1

  # check if we finished
  if len(sorted_order) == len(graph):
    print(sorted_order)

def main():
  print("Task Orders: ")
  print_orders(3, [[0, 1], [1, 2]])

  print("Task Orders: ")
  print_orders(4, [[3, 2], [3, 0], [2, 0], [2, 1]])

  print("Task Orders: ")
  print_orders(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])


main()

# O(V! * E) time complexity, where V is the number of verticies or tasks and E is the number of edges or prerequisites, since there are worst case V! combinations of tasks for V tasks.
# O(V! * E) space complexity since our recursive call stack is of size E and we can have V! combinations of outputs.
