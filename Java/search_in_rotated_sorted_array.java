/*
U
We are given an array where the elements were sorted but then they were rotated. We dont know how much it has been rotated.
    find the target value and return its index
    if it does not exist then return -1

M
Use binary search

P
find the pivot since there are two sections where we can use binary search
    when we find the pivot we will know where the two strictly increasing sections are
    the target will be in one of those 

Not rotated:
1 2 3 4 5 6 7
     mid

left rotated: pivot at the left side of the origin sorted array, A[mid] >= A[left]
3 4 5 6 7 1 2
     mid
search in A[left] ~ A [mid] if A[left] <= target < A[mid] else, search right side

right rotated: pivot at the right side of the origin sorted array, A[mid] < A[left]
6 7 1 2 3 4 5
     mid          
search in A[mid] ~ A[right] if A[mid] < target <= A[right] else, search left side
*/

class Solution {
    public int search(int[] nums, int target){
        if (nums.length == 0) {
            return 0;
        }
        
        int right = nums.length - 1;
        int left = 0;
        while (left <= right) {
            
            int mid = (left + right) / 2;
            
            if (nums[mid] == target) {
                return mid;
            }
            
            // left rotated
            if (nums[left] <= nums[mid]) {
                
                // target is in the left side
                if (nums[left] <= target && target < nums[mid]) {
                    right = mid - 1;
                }
                else {
                    left = mid + 1;
                }
                
            }
            else { // right rotated
                
                // target is in the right side
                if (nums[right] >= target && target > nums[mid]) {
                    left = mid + 1;
                }
                else {
                    right = mid - 1;
                }
            }
            
        }
        
        return -1;
    }
}
