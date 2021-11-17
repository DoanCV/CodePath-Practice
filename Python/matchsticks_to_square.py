"""
We are given an array of matchsticks
    use all of them to form a square
    you cannot break sticks but can link them together and can only use each one time

We know that the sum of all the lengths has to be divisble by four otherwise our perimeter cannot be a square

DFS backtracking

we can map out all four sides of the square since we can put sticks there
    we will have to backtrack when we find that we went over the length of the side
    that way we can try other placements

we will know when we are done when all the sticks have been used and we have not gone over
    if one search is True there is a way to make the square else False
    we only need one search to return True to return True

O(4^N) time complexity where N is the length of the given array of matches. At each step in our search, we can try to place the current stick in the four sides.
O(N) space complexity since that is the height of our recursive call stack.
"""

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
                
        side_length = sum(matchsticks) // 4
        sides = [0 for _ in range(4)]
        
        if sum(matchsticks) / 4 != side_length:
            return False
        
        # optimization heuristic: sort in reverse order, if we find a stick longer than the side_length it is impossible to make a square
        matchsticks.sort(reverse = True)
        
        def backtrack(index):
            if index == len(matchsticks):
                return True
        
            for i in range(4):
                
                # check if we can add the current stick to the current side
                if matchsticks[index] + sides[i] <= side_length:
                    sides[i] += matchsticks[index]
                    if backtrack(index + 1):
                        return True
                    sides[i] -= matchsticks[index]
                
            return False

        
        return backtrack(0)
