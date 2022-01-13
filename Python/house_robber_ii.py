"""
We can use the same algo from house robber I
    however since it is circular we can either skip the first house and come back to it later since the array is circular or skip it altogether
    if we apply the same algo on these two and take the maximum, we will have our answer

"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def house_robber(nums):
            house1 = 0
            house2 = 0
            
            for house in nums:
                temp = house1
                house1 = max(house + house2, house1)
                house2 = temp
            
            return house1
        
        return max(nums[0] + house_robber(nums[2:-1]), house_robber(nums[1:]))
