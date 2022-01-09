class Solution {
public:
    int maximumSwap(int num) {
        string numstr = to_string(num);
        
        int max_digit = -1;
        int max_digit_index = -1;
        int left_index = -1;
        int right_index = -1;
        
        for (int i = numstr.size() - 1; i > -1; i--) {
            
            // update max
            if (numstr[i] > max_digit) {
                max_digit = numstr[i];
                max_digit_index = i;
                continue;
            }
            
            if (numstr[i] < max_digit) {
                left_index = i;
                right_index = max_digit_index;
            }
            
            // if they are equal do not update since we want the largest possible answer 
        }
        
        // if the digits are already in descending order
        if (left_index == -1) {
            return num;
        }
        
        swap(numstr[left_index], numstr[right_index]);
        
        return stoi(numstr);
    }
};
