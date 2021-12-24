#include <bits/stdc++.h>

using namespace std;

class solution{

  vector<vector<int>> graph;

public:
  solution(vector<vector<int>> &graph){
    this->graph = graph;
  }

  bool knows(int a, int b){
    return graph[a][b];
  }

  int find_celebrity(int N){

    stack<int> candidates;
    for (int i = 0; i < N; i++) {
      candidates.push(i);
    }

    while (candidates.size() > 1) {
      int candidate = candidates.top();
      candidates.pop();
      int person = candidates.top();
      candidates.pop();

      if (knows(candidate, person)) {
        candidates.push(person);
      }
      else {
        candidates.push(candidate);
      }
    }

    int candidate = candidates.top();
    for (int i = 0; i < N; i++) {
      if (candidate != i && (knows(candidate, i) || !knows(i, candidate))) {
        return -1;
      }
    }

    return candidate;
  }

};

int main() {
  vector<vector<int>> v = {{1,1,0},{0,1,0},{1,1,1}};
  solution obj(v);
  cout << obj.find_celebrity(3);
} 
