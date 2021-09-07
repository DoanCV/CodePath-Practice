"""
Topological sort
      if we have a valid sort then we have a directed acyclic graph which makes the schedule valid
      treat prereqs as edges and tasks as verticies

store graph in adjacency list
      hashmap = {vertex number (can use default dict) : list of children}

store inDegree count
      hashmap = {vertex number (can use default dict) : frequency}

use a queue to sort
      traverse graph in bfs fashion
      add sources to queue and then subtract 1 from children inDegree count

if there is nothing left in the queue then we have DAG and return True otherwise return False
"""

from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # case 0: tasks <= 0
        if numCourses <= 0:
              return False

        # create adjacency list
        graph = {i : [] for i in range(numCourses)}

        # get inDegree
        inDegree = {i : 0 for i in range(numCourses)}

        # build graph
        for edge in prerequisites:
            parent, child = edge[0], edge[1]

            graph[parent].append(child)

            inDegree[child] += 1

        # add first level (sources) to queue
        queue = deque()
        for key, value in inDegree.items():
              if value == 0:
                queue.append(key)

        # bfs
        sorted_order = []
        while queue:

            curr_vertex = queue.popleft()
            sorted_order.append(curr_vertex)

            for child in graph[curr_vertex]:
                inDegree[child] -= 1

                if inDegree[child] == 0:
                    queue.append(child)

        # if the shcedule is has all of the tasks then it is valid
        return len(sorted_order) == numCourses
      
"""
Grokking version
"""

from collections import deque

def is_scheduling_possible(tasks, prerequisites):
      # case 0: tasks <= 0
      if tasks <= 0:
            return False

      # create adjacency list
      graph = {i : [] for i in range(tasks)}

      # get inDegree
      inDegree = {i : 0 for i in range(tasks)}

      # build graph
      for edge in prerequisites:
            parent, child = edge[0], edge[1]

            graph[parent].append(child)

            inDegree[child] += 1
      
      # add first level (sources) to queue
      queue = deque()
      for key, value in inDegree.items():
            if value == 0:
                  queue.append(key)

      # bfs
      sorted_order = []
      while queue:

            curr_vertex = queue.popleft()
            sorted_order.append(curr_vertex)

            for child in graph[curr_vertex]:
                  inDegree[child] -= 1

                  if inDegree[child] == 0:
                        queue.append(child)

      # if the shcedule is has all of the tasks then it is valid
      return len(sorted_order) == tasks

def main():
  print("Is scheduling possible: " +
        str(is_scheduling_possible(3, [[0, 1], [1, 2]])))
  print("Is scheduling possible: " +
        str(is_scheduling_possible(3, [[0, 1], [1, 2], [2, 0]])))
  print("Is scheduling possible: " +
        str(is_scheduling_possible(6, [[0, 4], [1, 4], [3, 2], [1, 3]])))

main()
