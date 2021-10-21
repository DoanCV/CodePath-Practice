class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # the difference from what we currently have (the sum) to what we want (n times the minimum) is the number of moves
        return sum(nums) - len(nums) * min(nums)
