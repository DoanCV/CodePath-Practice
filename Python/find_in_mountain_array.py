# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

"""
We are given a mountain array
    there exists a peak where the elements from the start to the peak is ascending order and the elements from the peak to the end is in descending order

we have to interface with the mountain array so we have two methods
    MountainArray.length()
    MountainArray.get()
    
run binary search to find the peak
    if the target is the peak then we are done

run binary search on the left of the peak
    we can use the peak as our right side
    if we find the target then we are done
        we run left first since we want the minimum index

run binary search on the right of the peak
    we can use the peak as our left side
    if we find the targe then we are done
    
after these searches we are done since we cant find the target so return -1


# we are limited to 100 calls to MountainArray.get()
# our max size mountain array is 10,000 which is 100^2
# binary search -> O(logN) time so we are safe
"""

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        mountain_size = mountain_arr.length()
        
        left = 0
        right = mountain_size - 1
        
        # there is always a peak since we always have a mountain array so use < instead of <=
        while left < right:
            
            mid = (left + right) // 2
            
            # not asecending
            if mountain_arr.get(mid) >= mountain_arr.get(mid + 1):
                right = mid
            # we are past the peak
            else:
                left = mid + 1
            # print('0:', mid)
        
        
        peak = left
        if mountain_arr.get(peak) == target:
            return peak
        
        # search left side
        # use <= instead of < since we may not have the target at all
        left = 0
        right = peak - 1
        while left <= right:
            
            mid = (left + right) // 2
            # print('1:', mid)
            mid_val = mountain_arr.get(mid)
            
            if mid_val < target:
                left = mid + 1
            elif mid_val > target:
                right = mid - 1
            else:
                return mid
        
        # search right side
        # we know everything is in descending order so flip the logic inside the wile loop
        left = peak + 1
        right = mountain_size - 1
        while left <= right:
            
            mid = (left + right) // 2
            # print('2:', mid)
            mid_val = mountain_arr.get(mid)
            
            if mid_val < target:
                right = mid - 1
            elif mid_val > target:
                left = mid + 1
            else:
                return mid
        
        return -1
