"""
If sum of remaining numbers is greater than or equal to the maximum milestone then maximum milestone can be completed along with other milestones. Otherwise, maximum milestone cannot be reached as it will go till the sum of remaining milestones

O(N) time complexity where N is the length of the given array since we calculate the sum and find the max. This can be done in one loop but I uses a standard library function.
O(1) space complexity since I do not use any extra data structures.
"""
class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        max_milestone = max(milestones)
        sum_milestone = sum(milestones)
        
        if sum_milestone - max_milestone >= max_milestone:
            return sum_milestone
        else:
            return 2 * (sum_milestone - max_milestone) + 1
