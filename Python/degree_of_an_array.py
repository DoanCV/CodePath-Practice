"""
U
the degree of an array is the maximum frequency of any one of its elements

we need to find the length of the shortest subarray with the same degree as the entire array

M
we can get the degree by finding the maximum frequency

with this we can use a sliding window to find the smallest length subarray
    in our window we check the degree in a hashmap as well
        when we the degree we shrink and find the smallest

P
find the max frequency

loop through array with window_end
    
    add 1 to the frequency of the window_end character
    
    if the window_end character frequency is equal to the degree
        
        update the length of the subarray
        
        move window_start

I
See class below

R
This solution handles the case where the entire array is the shortest subarray since that would mean our min_len is the length of the given array

E
O(N) time complexity, where N is the length of the given array, since we solve in two passes.
O(N) space complexity since in the worst case every number is unique so our hashmap size is equal to the length of the given array.
"""

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        
        # get degree
        freq_map = {}
        degree = 0
        for i in range(len(nums)):
            curr_number = nums[i]
            
            if curr_number not in freq_map:
                freq_map[curr_number] = 0
                
            freq_map[curr_number] += 1
            
            if freq_map[curr_number] > degree:
                degree = freq_map[curr_number]
                
                
        # find minimum length subarray
        window_start = 0
        min_len = len(nums)
        hashmap = {}
        for window_end in range(len(nums)):
            
            curr = nums[window_end]
            
            # add to hashmap
            if curr not in hashmap:
                hashmap[curr] = 0
            hashmap[curr] += 1
            
            while hashmap[curr] == degree:
                
                if window_end - window_start + 1 < min_len:
                    min_len = window_end - window_start + 1
                    
                hashmap[nums[window_start]] -= 1
                
                window_start += 1
        
        return min_len
