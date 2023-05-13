class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        """
        keep track of the number of possible strings from length 0 to high
        even if low is not 0 we build our answer up
            there is only one way to have 0 length string so we use that as base case

        """
        MOD = 10**9 + 7
        result = 0

        dp = [0 for _ in range(high + 1)]
        dp[0] = 1

        for i in range(1, high + 1):
            if i >= one:
                dp[i] = dp[i] + dp[i - one]
            
            if i >= zero:
                dp[i] = dp[i] + dp[i - zero]
            
            if i >= low:
                result = result + dp[i]

        return result % MOD
