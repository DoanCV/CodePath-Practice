# Brute force is probably the best way, most greedy methods miss the test case that simulates this insane clip: https://www.youtube.com/watch?v=kBbGptm9v7A

class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        @lru_cache(None)
        def clean(baord):
            # sliding window to crush like in 1D candy crush
        
        @lru_cache(None)
        def dfs(board, hand):
            if not board:
                return 0
            if not hand:
                return float('inf')
            
            
            m = len(board)
            ans = float('inf')
            for j, b in enumerate(hand):
                new_hand = hand[:j] + hand[j+1:]
                for i in range(m + 1):
                    new_board = clean(board[:i] + b + board[i:])
                    ans = min(ans, 1 + dfs(new_board, new_hand))
            return ans
        
        
        ans = dfs(board, hand)
        
        if ans < float('inf'):
            return ans
        else:
            return -1
