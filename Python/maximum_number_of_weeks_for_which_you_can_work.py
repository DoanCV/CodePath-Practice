"""
If sum of remaining numbers is greater than or equal to the maximum milestone then maximum milestone can be completed along with other milestones. Otherwise, maximum milestone cannot be reached as it will go till the sum of remaining milestones

O(N) time complexity where N is the length of the given array since we calculate the sum and find the max. This can be done in one loop but I uses a standard library function.
O(1) space complexity since I do not use any extra data structures.

ex. [5,2,1]
[4,2,1] steps = 1
[4,1,1] steps = 2
[3,1,1] steps = 3
[3,0,1] steps = 4
[2,0,1] steps = 5
[2,0,0] steps = 6
[1,0,0] steps = 7
we have to stop here since we cant do project 0 twice in a row
"""
class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        max_milestone = max(milestones)
        sum_milestone = sum(milestones)
        
        
        # if we can finish all of them
        if sum_milestone - max_milestone >= max_milestone: 
            return sum_milestone
        
        # we can only finish everything else plus the same amount out of the project with the most milestones, + 1 since we can start with the max and alternate
        else: 
            return 2 * (sum_milestone - max_milestone) + 1
