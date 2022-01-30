"""
A cinema has n rows of seats, numbered from 1 to n and there are ten seats in each row, labelled from 1 to 10
    allocate seats and return the maximum number of four person groups that you can assign    

at most we can only seat two families in each row
    therefore we have at most 2*n families that can be seated

Use a hashmap to store a flag for each row
    we know that we need 4 in a row to allocate
    the spacing is as follows
    
        1-3 4-7 8-10
        
        however the exception says that we can reserve 2-5 and 6-9 if they are all free
            that is why we use three flags since 2-5 and 6-9 are the only ways we can have 4 seat groups apart from 4-7
            we have to consider what will happen if 4-5 and 6-7 are already reserved since that clearly eliminates our max possible seating allocation
    
"""
from collections import defaultdict
class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        
        seats = defaultdict(set)
        
        for row, column in reservedSeats:
            
            if column in [2,3,4,5]:     # we dont care about 1 and 10 since we cant put a 4 group there anyways
                seats[row].add(0)       # the flag value doesnt matter since we will use the size to determine the state of the row
            if column in [4,5,6,7]:
                seats[row].add(1)
            if column in [6,7,8,9]:
                seats[row].add(2)
            
        max_seats = 2 * n
        for row in seats:
            if len(seats[row]) == 3:    # we cant put a group of 4 in the row at all
                max_seats -= 2
            else:
                max_seats -= 1          # the key exists so that means one group can be placed
                
        return max_seats
