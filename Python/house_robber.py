"""
this is just fibonacci

robbery of current house + loot from houses before the previous
loot from the previous house robbery and any loot captured before that

we can do this iteratively
    either with array storing previous house robberies or just use two varaibles and get O(1) space
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        house1 = 0
        house2 = 0
        
        for house in nums:
            temp = house1
            house1 = max(house2 + house, house1)
            house2 = temp
        
        return house1
