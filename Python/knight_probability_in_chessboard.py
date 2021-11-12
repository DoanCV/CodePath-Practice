"""
First thought is to DFS all the possible moves, 8 of them (we can map out the coordinate changes)
    we need to find the probability that after k moves the knight will still be on the board
        each move we add the probability since a move is an event so the final event plus the previous is our answer
    
    potential issue: we have already visited a square, why repeat the moves unless we have to take more steps, we can keep track of old answers
    
    
we start with 0 steps and then build up to k or when we are out of bounds
memoize with a hashmap
    {(row, column, steps_taken): probability}

O(8^k) time complexity where k is the number of moves that we are trying to calculate the probability for. For each square that we visit we have 8 moves and we take k steps. Each step creates 8 more. We are capped by the size of the given baord.
O(8^k) space complexity since our hashmap size is equal to the number of unique moves that we visited. Realistically we could revisit squares with the same number of steps taken so far making the actual answer less that what I am suggesting.
"""
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        # "L" shape movement
        moves = [[-2,1], [-1,2], [2,1], [1,2], [2,-1], [1,-2], [-1,-2], [-2,-1]]
        
        # memoize
        memo = {}
        
        def dfs(steps_taken, x, y, curr_probability):
            
            probability = 0.0
            
            # if we are inside the board
            if x >= 0 and x < n and y >= 0 and y < n: 
                
                # case: we have not made k moves
                if steps_taken < k:
                    
                    # try all 8 moves and store probability
                    for dx, dy in moves:
                        
                        next_x = x + dx
                        next_y = y + dy
                        
                        if (next_x, next_y, steps_taken + 1) not in memo:
                            memo[(next_x, next_y, steps_taken + 1)] = dfs(steps_taken + 1, next_x, next_y, curr_probability / 8)
                           
                        probability += memo[(next_x, next_y, steps_taken + 1)] # add the event probabilities 
                    
                # case: we mad k total moves so we are done
                else:
                    probability = curr_probability
            
            # else we are out and the probability will be 0
            return probability
            
            
        return dfs(0, row, column, 1.0)
