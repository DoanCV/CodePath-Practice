class Solution {
public:
    void dfs(vector<int> nums, vector<vector<int>> &result, int pos){
        if (pos == nums.size() - 1) {
            result.push_back(nums);
        }
        else {
            for (int i = pos; i < nums.size(); i++){
                // if the values are not equal or the indices are the same then we know we can create a unique permutation
                if (i == pos || (nums[i] != nums[pos])){
                    swap(nums[pos], nums[i]); // we dont swap back since our if staetment already prevents duplicates
                    dfs(nums, result, pos + 1);
                }
            }
        }
    }
    
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> result;
        dfs(nums, result, 0);
        return result;
    }
};
