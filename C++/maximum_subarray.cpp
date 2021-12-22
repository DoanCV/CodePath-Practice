// the header files of header files
#include <bits/stdc++.h>

using namespace std;

class solution {
private:
  int max_subarray(vector<int> &nums) {
    int max_subarray_sum = nums[0];
    int local_max = nums[0];
    
    for (int i = 1; i < nums.size(); i++) {
      local_max = local_max + nums[i];
      local_max = max(nums[i], local_max);

      max_subarray_sum = max(local_max, max_subarray_sum);
    }
    
    return max_subarray_sum;
  }

};
