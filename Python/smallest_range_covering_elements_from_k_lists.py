"""
U
we are given k lists, not all the same length

each list is sorted in non-decreasing order
    this means we can have duplicate numbers
    
we need to find the smallest (shortest) range of numbers that includes at least one number from each list

output the start and end of the range
    because each list has at least one number, we are never going to have an invalid input
    all our values are integers, can be negative
    k cant be negative

M
ex.
nums = [[4,10,15,24,26],
        [0,9,12,20],
        [5,18,22,30]]

ans = [20,24]
because
        [[4,10,15,(24),26],
        [0,9,12,(20)],
        [5,18,(22),30]]

we can brute force by checking every possible range
    generate all ranges aka pairs of values then run through each pair and check if it is valid and find the smallest
    O(N^3) time N^2 for generating pairs and N for checking, N is the total number of elements in our lists

instead we can use a heap
    we know at least one number has to come from each list
    we can have a pointer on each list and then increment the minimum of the pointers to try and close the range
    
    to keep track of the ranges that we check, we need to find the minimum and maximum of our pointers
        we are using a min_heap so the top will be our minimum
        we will have a variable to compare each number that we are adding to our range
        
        if the length of the range is less then we update the smallest (shortest) range
        
P
for each list in nums
    add the first element to out min_heap
        we store the value as priroity and its respective index to reference when needed
    we find the maximum from these pointers since that will be our maximum for our first range

calculate our first range

# we can stop checking when we hit the end of a list
while heap is not empty
    
    pop the top of our heap
    add its next value to the heap
        if this value is greater than our max update it
        after adding check our min and update if necessary
        
    if there is no next value then we are done
    
    else calculate the range
        if the range is smaller than what we have so far update it

return the answer
    
I
See solution class below

R
[[4,10,15,24,26],
[0,9,12,20],
[5,18,22,30]]

[0,4,5]
range_maximum = 5
range_minimum = 0
[0,5] min_size = 5

[4,5,9]
range_maximum = 9
range_minimum = 4
[4,9] min_size = 5

[5,9,10]
range_maximum = 10
range_minimum = 5
[5,10] min_size = 5

[9,10,18]
range_maximum = 18
range_minimum = 9
[5,10] min_size = 5

...this works...


E
O(NlogK) time complexity, where N is the length of the shortest list and k is the number of list in nums. Our heap is size k and when we pop and push the rebalancing takes O(logK) time. In the worst case we do this as many times as the shorted list length. However, this scales linearly with the size of the array.

"""
from heapq import *
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        min_heap = []
        
        range_maximum = -10**5 - 1
        range_minimum = 10**5 + 1
        
        for num_list in nums:
            
            heappush(min_heap, (num_list[0], 0, num_list))
            
            if num_list[0] > range_maximum:
                range_maximum = num_list[0]
            
            if num_list[0] < range_minimum:
                range_minimum = num_list[0]
        
        min_pair = [range_minimum, range_maximum]
        min_pair_size = range_maximum - range_minimum
        
        while min_heap:
            
            curr_val, curr_index, curr_list = heappop(min_heap)
            
            # we are at the end of a list
            if curr_index + 1 > len(curr_list) - 1:
                return min_pair
                
            else:
                next_val = curr_list[curr_index + 1]
                
                if next_val > range_maximum:
                    range_maximum = next_val
                
                heappush(min_heap, (next_val, curr_index + 1, curr_list))
                
                if min_heap[0][0] > range_minimum:
                    range_minimum = min_heap[0][0]
                    
                if range_maximum - range_minimum < min_pair_size:
                    min_pair_size = range_maximum - range_minimum
                    min_pair = [range_minimum, range_maximum]

        return min_pair
