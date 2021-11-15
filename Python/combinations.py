"""
DFS with a helper function

    keep building up to k length
        when we are done add a copy so that we can backtrack and try finish building the next combination
        
    build by trying every number from current to the end
        recurse with the current combination
        backtrack so that we can continue with the next value that we are trying in our loop from current to end

O(C(n,k)) time complexity where n is the number of values we can use to build the combinations and k is the length of a valid combination. This is the number of combinations where we have n elements and we choose k of them.
O(C(n,k)) space complexity since that is the number of combinations that we have and are storing in the combinations array.
"""
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = []
        self.helper(1, [], n, k, combinations)
        return combinations
        
    def helper(self, curr_position, curr_combination, n, k, combinations):
        
        if len(curr_combination) == k:
            combinations.append(curr_combination[:]) # append a copy of the current combination otherwise backtracking will get us nothing
            return
            
        for position in range(curr_position, n + 1):
            curr_combination.append(position)
            self.helper(position + 1, curr_combination, n, k, combinations) # recurse            
            curr_combination.pop() # backtrack
