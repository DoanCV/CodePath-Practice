class Solution:
    def trap(self, height: List[int]) -> int:
        """
        we know there must be a positive value height to bound water on two sides of the current building
        
        relative to the height of the current building, we need to know out of the highest buildings, which is the lowest to bound the water
        
        the difference between this minimum height and the current height is the amount of water that is trapped vertically along this building
        
        we will keep track of the sum to return
        """
        
        # the number of buildings is the length of the giveen height array
        buildings_count = len(height)
        
        # there must be at least 3 building for water to get trapped
        if buildings_count <= 2:
            return 0
        
        # get the max heights from the left
        leftMax = [0] * buildings_count
        max_height = 0
        for i in range(buildings_count):
            max_height = max(max_height, height[i])
            leftMax[i] = max_height
        
        # get the max heights from the right 
        rightMax = [0] * buildings_count
        max_height = 0
        for i in range(buildings_count - 1, -1, -1):
            max_height = max(max_height, height[i])
            rightMax[i] = max_height
        
        # calculate the trapped water height
        sum = 0
        for i in range(buildings_count):
            sum += min(leftMax[i], rightMax[i]) - height[i]
        
        return sum

      
# O(N) time complexity, where N is the length of the given height array, since we traverse the array three times in a linear fashion with single loops.
# O(1) space complexity since we are not using any extra data structures.
