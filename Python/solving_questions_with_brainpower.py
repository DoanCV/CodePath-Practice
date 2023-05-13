class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        """
        have to start at problem zero and go in order
            we can skip questions if its not worth it
            if we choose to do problem i we cant do the next question[i][1] of problems
        
        dp = [most points up to the current problem]

        dp[0] has our answer, start from the end
        dp[len(questions)] = 0 is the base case so that if you choose to skip the first question u dont get out of bounds
        
        skip the current problem
        dp[i] = dp[i+1] 

        do the current problem
        dp[i] = dp[questions[i][1] + i + 1] + questions[i][0]
        """
        dp = [0 for _ in range(len(questions) + 1)]

        for i in range(len(questions) - 1, -1, -1):
            points = questions[i][0]
            skip = questions[i][1]

            # avoid going out of bounds
            # min(skip + i + 1, len(questions))
            dp[i] = max(dp[min(skip + i + 1, len(questions))] + points, dp[i + 1]) 

        return dp[i]
