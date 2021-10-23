"""
Recursive DFS

no two stones are in the same position
store stones' positions in a hashmap
    however since the tuple reprsenting the positions are both integers we will need to differentiate row position from column position
    
we can group stones to remove by checking if there are stones in the same column or row
    the most stones removed is the difference between the number of stones and the number of groups that we found
    we have to leave out one single node because based on the question, there has to be one more node belonging to the same group as the node in reference


main()
    we create our row and column hashmaps
    
    then for each stone we will call our helper to start a search if the stone has not already been visited
        each search means that we found a group
        
    return the difference between the number of stones and the number groups
    

helper()
    we feed in a stone's position

    look through

O(N^2) time complexity where N is the number of stones. We loop through each stone's row and column and then through those of its group. Creating our hashmap is linear.
O(N) space complexity since that is the size of both our hashmaps and also in the worst case our set. We visit every stone but they are arranged diagonally so we visit all of them but we have nothing to remove.
"""
from collections import defaultdict
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        rows = defaultdict(list)
        columns = defaultdict(list)
        
        for i, j in stones:
            rows[i].append(j)
            columns[j].append(i)
            
        visited = set()
        
        def helper(i, j):
            for column in rows[i]:
                if (i, column) not in visited:
                    visited.add( (i, column) )
                    helper(i, column)
            
            for row in columns[j]:
                if (row, j) not in visited:
                    visited.add( (row, j) )
                    helper(row, j)
                
            
        group_count = 0    
        for i, j in stones:
            if (i, j) not in visited:
                helper(i, j)
                group_count += 1
            
        return len(stones) - group_count
