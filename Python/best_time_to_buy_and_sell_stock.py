class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        sliding window        
        """
        
        max = 0
        window_start = 0
        for window_end in range(len(prices)):
            profit = prices[window_end] - prices[window_start]
            
            if profit > max:
                max = profit
            
            if prices[window_start] > prices[window_end]:
                prices[window_start] = prices[window_end]
        
        return max
      
# O(N) time complexity, where N is the length of the given array. We are using sliding window to traverse through the array once.
# O(1) space complexity since we are not using any extra data structures.
