/*
We start from the edge and try to flag every position for each ocean with DFS
    then we take the intersection of the searches, if the position shows up in both scans then we know that it will work

use a visited boolean array to denote if the position has been visited
    we can move up, down, left, right and since we are starting from the edge we can only move if the next value is greater than or equal to the current value

O(m * n) time complexity where m is the number of rows and n is the number of columms. We search through each position of the given matrix several times in the worst case.
O(m * n) space complexity sicne we create two boolean matricies to keep track of what positions reach the pacific ocean and atlantic ocean.
*/

class Solution {
public:
    int m;
    int n;
    
    vector<vector<bool>> atlantic;
    vector<vector<bool>> pacific;
    vector<vector<int>> coordinates;
    
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        
        if (!heights.size()) {
            return coordinates;
        }
            
        m = heights.size();
        n = heights[0].size();
        
        atlantic = vector<vector<bool>> (m, vector<bool>(n, false));
        pacific = vector<vector<bool>> (m, vector<bool>(n, false));
        
        for (int i = 0; i < m; i++) {
            dfs(heights, pacific, i, 0);
            dfs(heights, atlantic, i, n - 1);
        }
        for (int i = 0; i < n; i++) {
            dfs(heights, pacific, 0, i);
            dfs(heights, atlantic, m - 1, i);
        }
        
        return coordinates;
    }
    
    void dfs(vector<vector<int>> &heights, vector<vector<bool>> &visited, int i, int j){
        if (visited[i][j]){
            return;
        }
        
        visited[i][j] = true;
        
        if (atlantic[i][j] && pacific[i][j]) {
            coordinates.push_back(vector<int>{i,j});
        }
        
        // dfs in four directions if the height is greater and 
        if (i + 1 < m && heights[i + 1][j] >= heights[i][j]){
            dfs(heights, visited, i + 1, j);
        }
        
        if (i - 1 >= 0 && heights[i - 1][j] >= heights[i][j]){
            dfs(heights, visited, i - 1, j);
        }
        
        if (j + 1 < n && heights[i][j + 1] >= heights[i][j]){
            dfs(heights, visited, i, j + 1);
        }
        
        if (j - 1 >= 0 && heights[i][j - 1] >= heights[i][j]){
            dfs(heights, visited, i, j - 1);
        }
    }
};
