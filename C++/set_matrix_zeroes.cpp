/*
O(N * M) time complexity where N is the number of rows and M is the number of columns in the given matrix. We solve with two full scans of the given matrix. 
O(1) space complexity since we solve in place. We use the first row and column to store if the entire column or row should be all zeros after a scan.
*/

class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        int row_count = matrix.size();
        int column_count = matrix[0].size();
        
        // use the first row and column to store if there is a zero at all
        bool first_row_has_zero = false;
        bool first_column_has_zero = false;
        
        // scan through one and mark the first row and column if we see a 0
        for (int row = 0; row < row_count; row++) {
            for (int column = 0; column < column_count; column++) {
                
                if (matrix[row][column] == 0){
                    
                    // mark the flag
                    if (row == 0){
                        first_row_has_zero = true;
                    }
                    if (column == 0){
                        first_column_has_zero = true;
                    }
                    
                    matrix[row][0] = 0;
                    matrix[0][column] = 0;
                }
                
            }
        }
        
        
        // flip everything but the first row and column to 0, we save the first row and column for later once we are done
        
        for (int row = 1; row < row_count; row++) {
            for (int column = 1; column < column_count; column++) {
                
                if (matrix[row][0] == 0 || matrix[0][column] == 0) {
                    matrix[row][column] = 0;
                }
                
            }
        }
        
        if (first_row_has_zero) {
            for (int column = 0; column < column_count; column++) {
                matrix[0][column] = 0;
            }
        }
        
        if (first_column_has_zero) {
            for (int row = 0; row < row_count; row++) {
                matrix[row][0] = 0;
            }
        }
        
    }
};
