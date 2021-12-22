#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class solution {
public:
  vector<int> two_sum(vector<int> &nums, int target) {
    unordered_map<int,int> differences;
    for (int i = 0; i < nums.size(); i++) {
      if (differences.count(target - nums[i])) {
        return {differences[target - nums[i]], i};
      }

      differences[nums[i]] = i;
    }

    return {-1,-1};
  }

};

int main(int argc, char* argv[]) {
  vector<int> nums = {2,7,11,15};
  solution test;
  auto result = test.two_sum(nums, 9);
  for (int i = 0; i < result.size() ; i++){
    cout << result[i] << " ";
  }
} 





// Using pair class

/*
#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class solution {
public:
  static pair<int, int> two_sum(vector<int> &nums, int target) {
    unordered_map<int,int> differences;
    for (int i = 0; i < nums.size(); i++) {
      if (differences.count(target - nums[i])) {
        return make_pair(differences[target - nums[i]], i);
      }

      differences[nums[i]] = i;
    }

    return {-1,-1};
  }

};

int main(int argc, char* argv[]) {
  vector<int> nums = {2,7,11,15};
  auto result = solution::two_sum(nums, 9);
  cout << result.first << ", " << result.second;
}
*/