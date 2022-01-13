"""
top down DP
    memoization with hashmap storing states
    a state is defined by the current sum and the current index
        start from the target and subtract or add the current value

"""
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        self.nums = nums
        self.target = target
        
        self.memo = {}

        return self.dfs(0, 0)
    
    def dfs(self, index, curr_sum):
        
        if (index, curr_sum) in self.memo:
            return self.memo[(index, curr_sum)]
        
        # base case
        # invalid index and we used all of our numbers in num
        if index >= len(self.nums) and curr_sum == self.target:
            return 1
        
        if index >= len(self.nums):
            return 0
        
        positive = self.dfs(index + 1, curr_sum + self.nums[index])
        negative = self.dfs(index + 1, curr_sum - self.nums[index])
        
        self.memo[(index, curr_sum)] = positive + negative
        return self.memo[(index, curr_sum)]
