"""
ex.
prices = [7,1,5,3,6,4]


window_end = 0
max = 0
window_start = 0
    bc 7-7 = 0 


window_end = 1
max = 0
    bc 1 - 7 < 0
window_start = 1
    bc prices[window_start] > prices[window_end]


window_end = 2
max = 4
    bc 5 - 1 = 3 and is > 0
window_start = 1


window_end = 3
max = 4
    3 - 1 = 2 < 4
window_start = 1


window_end = 4
max = 5
    6 - 1 = 5 and is > 4
window_start = 1


window_end = 5
max = 5
    4 - 1 = 3 and is < 5
window_start = 1


The idea is that we are trying to get window_start to the lowest value possible and then window_end to the highest value possible
    all in one pass

"""

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
