class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        
        dp = {}
        
        
        def dfs(curr_house, curr_target, prev_color):
            key = (curr_house, curr_target, prev_color)
            
            
            # base case: color 0 houses
            # only out of houses check is necessary
                # we can also check if the target neighborhood is done
            if curr_house == len(houses) or curr_target < 0 or m - curr_house < curr_target:
                return 0 if curr_target == 0 and curr_house == len(houses) else float("inf")
            

            # if key not in cache
            if key not in dp:
                
                # unpainted
                    # either paint the current house like the previous one or make it a different color to get closer to the target
                if houses[curr_house] == 0:
                    dp[key] = min(dfs(curr_house + 1, curr_target - (color != prev_color), color) + cost[curr_house][color - 1] for color in range(1, n + 1))
                
                # painted
                    # move on we can't change the color
                else:
                    dp[key] = dfs(curr_house + 1, curr_target - (houses[curr_house] != prev_color), houses[curr_house])
                    
            
            return dp[key]
            
        result = dfs(0, target, -1)
        
        # too many neighborhoods, we cant paint over ones that were already painted
        return result if result < float("inf") else -1

"""
0 <= curr_house < m
0 <= curr_target <= target
1 <= curr_color <= n

O(m * target * n ^ 2) time complexity, where m is the number of houses, and n is the number of houses. There are m * target * n possible states but in our function call we loop for each possible color.
O(m * target * n) space complexity since that is the size of our cache, the hashmap containing the possible states.

"""
