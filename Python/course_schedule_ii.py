"""
topological sort

however, the second value in the given list of edges is the prereq not the first so we have to swap first and second
"""

from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course_plan = []
        
        # case 0: numCourses <= 0
        if numCourses <= 0:
            return course_plan 
        
        # initialize adjacency list
        graph = {i : [] for i in range(numCourses)}
        
        # initialize inDegree count map
        inDegree = {i : 0 for i in range(numCourses)}
        
        # build graph
        for course in prerequisites:
            parent, child = course[1], course[0]
            graph[parent].append(child)
            
            # also count inDegree
            inDegree[child] += 1
        
        # add sources to queue
        queue = deque()
        for key, value in inDegree.items():
            if value == 0:
                queue.append(key)
        
        # while the queue is not empty add sources to output list and then decrement the respective childrens inDegree by 1
        while queue:
            curr_class = queue.popleft()
            course_plan.append(curr_class)
            
            for child in graph[curr_class]:
                inDegree[child] -= 1
                
                if inDegree[child] == 0:
                    queue.append(child)
        
        
        # if the length of the output list is not equal to the number of coruses then we have a cycle so return an empty list
        if len(course_plan) != numCourses:
            return []
        
        # return the output list otherwise
        return course_plan

# O(V + E) time complexity, where V is the number of courses or verticies and E is the number of edges or prerequisite pairs, since we only build the graph once and access to remove each vertex once.
# O(V + E) space complexity since we store our edges and verticies in our adjacency list
