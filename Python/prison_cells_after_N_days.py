"""
8 prison cells
    the ones at the edges should be at 0 by the end
    by the time they become 0, we should be entering a cycle since the other 6 states can be 1 or 0
        we can cut down the number of times we check if we find a cycle
        
we will simulate the day changes and store the states in a hashmap
O(64) since we have 2^6 possible combinations so that is our worst case. We have 2 states for 8 slots. 
"""

class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        visited_states = {}
        
        while n > 0:
            curr_state = tuple(cells)
            
            # we found cycle so cut down out iterations
            if curr_state in visited_states:
                n = n % (visited_states[curr_state] - n)
            
            visited_states[curr_state] = n
            
            if n > 0:
                n -= 1
                cells = self.find_next_day_state(cells)
        
        return cells
    
    def find_next_day_state(self, cells):
        
        next_day_state = [0 for i in range(len(cells))]
        
        for i in range(1, len(cells) - 1):
            if cells[i - 1] == cells[i + 1]:
                next_day_state[i] = 1
            else:
                next_day_state[i] = 0
        
        return next_day_state
