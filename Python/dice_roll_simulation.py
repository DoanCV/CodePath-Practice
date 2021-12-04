"""
we have a generator to get us 1-6
    constraint: we cant roll the number more than x amount of times which is given in the array rollMax (1-indexed)
    
find the number of distinct sequences with n rolls

approach:

we will use a [n + 1][faces + 1] dimensional dp array
    the rows are the number of rolls so far
    columns 0 to faces - 1 represents the number of combinations there could be that at i-th rolling and the last face is the total number of sequences for i rolls
    
intuition from LC discuss
in the example
n = 3, rollMax = [1,1,1,2,2,3]

let's say we roll dice i = 5 times, and the last face is j = 5
we have this sequence xxxx5 where x could ranges from 0 to 5 arbitrarily if we are not restricted
let's calculate how many combinations we could form xxxx5 with constraint rollMax[j] = 3

step1: xxxy5, where x in [0, 5] and y in [0, 4], this means from the end 5, we have consecutive one 5
step2: xxy55, this means from the end 5, we have consecutive two 5
step3: xy555, this means from the end 5, we have consecutive three 5
We could not climb more columns because we are restricted to only be able to climb up rollMax[j] = 3 steps

Then the question is how to calculate the combinations of ...xy. Actually if you take a deeper look, what ...xy means is essentially: give me all the combinations as long as the last face is not 5. We don't care what x should be here because it is not restricted and could choose any value (it could be even same as y, or same as 5). As long as y is not equal to 5, we are good to go


O(n^2) time complexity where n is given. we loop through each row and for each row we go through all the faces, which there are 6. for each of these faces we go back up based on the max consecutive rolls. only n of these are significant since any more is meaningless. so in the worst case there are n of these so we have O(6n^2) we drop the constant. 

O(7*n) space complexity where 7 is the number of columns, 6 from the faces and 1 from the total. we have a 2d array of size [n + 1][faces + 1]
"""

class Solution:
    def dieSimulator(self, n, rollMax):
        faces = 6
        
        dp = [[0 for _ in range(faces + 1)] for _ in range(n + 1)] # [n + 1][faces + 1] dimensional dp array
        
        # base cases
        dp[0][faces] = 1 # there are 0 ways to roll any of the numbers so there is only 1 sequence which is an empty sequence
        dp[1][faces] = faces # if we have 1 roll then there are six sequences to roll a number since there are six faces
        for j in range(faces):
            dp[1][j] = 1 # when we have one roll there is only 1 way to roll a face this will add up to 6
            
        # calcaute the remaining rolls
        
        # for each number of roll
        for roll in range(2, n + 1):
            # search through every face
            for j in range(faces):
                
                # go up as far as we can
                for k in range(1, rollMax[j] + 1):
                    if roll - k < 0:
                        break
                    dp[roll][j] += dp[roll-k][faces] - dp[roll-k][j] # last column of the previous roll - value from previous roll and face 

            # update the last column
            dp[roll][faces] = sum(dp[roll])
            
        
        return dp[n][faces] % 1000000007
