/*
U
You start at the top left and want to get to the bottom right.
    You can only move one space at a time and either to the right or down

Determine the number of unique paths to get from start to finish

M
Bottom up DP

P
Store number of paths to get to position i,j starting from 0,0
    Base cases: 
        there is only one way to get to 0,0 from 0,0
        there is only one way to get to 0,j and i,0

E
O(m * n) time complexity where m is the number of rows and n is the number of columns. We visit each position once.
O(m * n) space complexity since we have an n*m dp grid.
*/
class Solution {
public:
    int uniquePaths(int m, int n) {
        vector<vector<int>> dp(m, vector<int>(n, 1));
        
        for (int i = 1; i < m; i++){
            for (int j = 1; j < n; j++){
                dp[i][j] = dp[i-1][j] + dp[i][j-1];
            }
        }
        
        return dp[m-1][n-1];
    }
};

// The space complexity can be further optimized since we arent really keeping track of each answer in the grid. We just have a single array of size min(m,n)
class Solution {
public:
    int uniquePaths(int m, int n) {
        vector<int> dp(n, 1);
        
        for (int i = 1; i < m; i++){
            for (int j = 1; j < n; j++){
                dp[j] += dp[j-1];
            }
        }
        
        return dp[n-1];
    }
};
