class Solution {
public:
    void dfs(vector<vector<int>> &combinations, vector<int> &curr_combination, int n, int k, int curr_position){
        
        if (curr_combination.size() == k) {
            combinations.push_back(curr_combination);
            return;
        }
        
        for (int i = curr_position; i <= n; i++){
            curr_combination.push_back(i);
            dfs(combinations, curr_combination, n, k, i + 1);
            curr_combination.pop_back();
        }
    }
    
    vector<vector<int>> combine(int n, int k) {
        vector<vector<int>> combinations;
        vector<int> curr_combination; 
        dfs(combinations, curr_combination, n, k, 1); // start at 1 since the range is [1,n]
        return combinations;
    }
};
