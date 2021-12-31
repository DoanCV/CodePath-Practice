"""
We are given a list of times and we need to find the minimum time difference

let:
p1 = 1:30
p2 = 10:46
p3 = 22:04

The distance from p1 to p3 is equal to abs(24:00 - 22:04 + 1:30)
The distance from p1 to p2 is equal to abs(1:30 - 10:46)
The distance from p2 to p3 is abs(10:46 - 22:04)

If we consider two points that are within (including) 12 hours of eachother and there's no crossing over the 0th hour, the calculation is straight forward and just abs (a-b). It gets complicated though in the other events. So how do we account for a distance greater than 12? Well, it means from the point which is larger, we need to do 24:00 - max(a,b) + min(a,b). The 24:00 - max(a,b) part offsets the max point back to 0, and then the min(a,b) part will get you to the destination. Therefore, we can conclude the general formula, dist(a,b) = min(abs(a - b), abs(24 - max(a,b) + min(a,b))

We can compare every pair of times but that is N^2 so instead sort and then compare adjacent values
    keep in mind we need to loop around so we have to compare the first and last times
    
O(NlogN) time complexity where N is the number of times in the given list. We sort all of the times and then we compare adjacent values in one pass.
"""

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        
        # convert into minutes to properly take differences
        for index, value in enumerate(timePoints):
            timePoints[index] = self.to_min(value)
            
        
        min_difference = float("inf")
        timePoints.sort()
        for i in range(len(timePoints) - 1):
            min_difference = min(min_difference, timePoints[i + 1] - timePoints[i])
            
            
        # wrap around
        # 24:00 - max(a,b) + min(a,b)
        min_difference = min(min_difference, 60 * 24 - timePoints[-1] + timePoints[0])
        
        return min_difference
    
    
    def to_min(self, time):
        time = time.split(":")
        result = 60 * int(time[0]) + int(time[1])
        return result
