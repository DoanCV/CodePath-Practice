"""
We can treat this like subarray sum equal to k

For each row, calculate the prefix sum

For each pair of columns, calculate the accumulated sum of rows
    loop through each column
        loop through the rest of the columns
        
            loop through each row for every pair of columns
                store prefix sum count frequency
                key of this hashmap present the unique value of all possible prefix sum that we've seen so far

O(m * n^2) time complexity where m is the number of rows and n is the number of columns in the given matrix. We have nested for loops. The outer two loops go through each column and then for each of those through the remaining columns. This is to calculate the prefix sum across the columns. For each pair we go loop through each row.
O(m) space complexity since we are using a hashmap. m is the number of keys in our hashmap
"""
from collections import defaultdict
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        
        # calculate prefix sum
        for curr_row in matrix:
            for column in range(1, n):
                curr_row[column] += curr_row[column - 1]
        
        # for every possible range between two columns, accumulate the prefix sum of submatrices that can be formed between these two columns by adding up the sum of values between these two columns for every row
        subarray_count = 0
        for i in range(n):
            for j in range(i, n):
                counter = defaultdict(int)
                counter[0] = 1
                
                curr_sum = 0
                for k in range(m):
                    
                    if i > 0:
                        curr_sum += matrix[k][j] - matrix[k][i - 1]
                    else:
                        curr_sum += matrix[k][j]
                    subarray_count += counter[curr_sum - target]
                    counter[curr_sum] += 1
        
        return subarray_count
