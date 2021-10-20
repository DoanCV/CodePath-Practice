"""
All values are distinct so we dont have to worry about ties

One pass
    Keep track of the max so far, if it wins k times then we have our answer
    if it loses then reset the streak
    
the max of the entire array will win no matter what but we have to consider k games so we may have a winner before we get to the absolute max
    if we do get to the end and we did not hit the streak then that means our current winner will win since that is the max value

O(N) time complexity where N is the length of the array or the number of players. We solve in one pass.
O(1) space complexity since we solve in place.
"""

class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        streak = 0
        winner = arr[0]
        
        for i in range(1, len(arr)):
            
            if arr[i] > winner:
                winner = arr[i]
                streak = 0

            streak += 1
            
            if streak == k:
                return winner
            
        return winner
