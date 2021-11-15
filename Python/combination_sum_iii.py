"""
DFS Backtracking

if we have the sum equal to n and k numbers then we have a valid combination
    otherwise we do nothing since the current combination isnt valid
    
we try to build the combination using numbers from 1 to 9
    start small and then build up
    backtrack for other possibilites

O(k * 9^k) time complexity where k is the length of valid combinations. We take O(k) time to create a copy to append to our valid combinations list. There are 9 numbers to choose from for each level in our search. We have O(k) levels since k is the length of our sequence.
O(k) space complexity if we do not include the list used for storing the number of combinations. We have k levels in our recursive call stack.
"""

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        solutions = []
        self.helper(1, [], solutions, k, n)
        return solutions
        
        
    def helper(self, curr_number, curr_combination, solutions, k, n):
        # when we have k numbers and the current combination sum is correct then we have a valid combination
        if len(curr_combination) == k and n == 0:
            solutions.append(curr_combination[:])
            return
        
        for i in range(curr_number, 10):
            # optimization: if we go over there is no point so we can skip the current search, this if statement will save us time
            if n - i >= 0:
                curr_combination.append(i) # build the combination
                self.helper(i + 1, curr_combination, solutions, k, n - i) # recurse
                curr_combination.pop() # backtrack
