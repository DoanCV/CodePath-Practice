class Solution {
public:
    vector<string> getFolderNames(vector<string>& names) {
        unordered_map<string, int> name_map;
        vector<string> results;
        
        for (int i = 0; i < names.size(); i++) {
            
            string curr_name = names[i];
            
            if (name_map.find(curr_name) == name_map.end()){
                name_map[curr_name] = 1;
                results.push_back(curr_name);
            }
            else {
                int count = name_map[curr_name];
                string temp = curr_name + "(" + to_string(count) + ")";
                
                while (name_map.find(temp) != name_map.end()) {
                    count++;
                    temp = curr_name + "(" + to_string(count) + ")";
                }
                
                name_map[temp] = 1;
                results.push_back(temp);
                name_map[curr_name] = count;
                
            }
        }
        
        return results;
    }
};
