/*
DFS backtracking

keep track of a list of combinations, a list that holds the current combination and the position in the given candidates array
  use a helper function
  
if the target is 0 then the current combination is valid
otherwise loop through the elements of the given candidates array starting from the current position and try out combinations
  pass in the current target - current value in the candidates array

*/

class Solution {
public:
    void combinationSum(vector<int> &candidates, int target, vector<vector<int>> &result, vector<int> &combination, int start){
        if (!target){
            result.push_back(combination);
            return;
        }
        
        for (int i = start; i < candidates.size() && target >= candidates[i]; i++) {
            combination.push_back(candidates[i]);
            combinationSum(candidates, target - candidates[i], result, combination, i);
            combination.pop_back();
        }
        
    }
    
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        vector<vector<int>> result;
        vector<int> combination;
        combinationSum(candidates, target, result, combination, 0);
        return result;
    }
};
