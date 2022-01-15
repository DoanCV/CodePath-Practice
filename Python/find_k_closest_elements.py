"""
binary search on the spacing between two pointers
    the pointers represent the range of k numbers that are closest to x, the given target

while we do not k numbers
    move the left pointer up if the value at the left pointer is further to the target than the right value is to the target
"""
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr) - 1
        
        while right - left >= k:
            
            if abs(arr[left] - x) > abs(arr[right] - x):
                left += 1
            else:
                right -= 1
            
        result = []
        for i in range(left, right + 1):
            result.append(arr[i])
        
        return result
