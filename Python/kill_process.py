"""
Problem:
we are given two lists
  the pid list has the processes which are nodes in a tree/graph
  the ppid list has the parent processes which reference other nodes in the tree
    if there is no parent, ie the node is the root itself, the ppid is 0

we are also given k, a process that we will kill
  we need to return a list of pid that are also killed because it depends on k

Ex
pid = [1,3,10,5]
ppid = [3,0,5,3]
k = 5

return [5,10] 
  order doesnt matter but we know this is correct since 10 is the only one that is dependent on 5 


we need to map the ppid to pid that depend on it
  hashmap = {ppid: [pid]}

we can then run BFS on it (iteratively)
  starting with looking through each dependent process from the pid that is going to get killed
    keep in mind not every pid is in ppid
    add what we see into a result array
"""
from collections import deque
def processes_killed(pid, ppid, k):
  hashmap = {}

  for index, value in enumerate(ppid):

    if value in hashmap:
      hashmap[value].append(pid[index])
    
    else:
      hashmap[value] = [pid[index]]

  

  queue = deque()
  queue.append( (k) )

  result = []
  while queue:
    
    curr_pid = queue.popleft()
    result.append(curr_pid)

    if curr_pid in hashmap:
      for child in hashmap[curr_pid]:
        queue.append(child)

    #else:
    #  continue

  return result

print(processes_killed([1,3,10,5], [3,0,5,3], 5))

