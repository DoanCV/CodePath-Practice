"""
we are given an array of integers, all positive
    return the integer such that when we change all the integers in the array that are larger than our output, the sum of all the elements is as close as possible to the target

Every number summed up should be close or equal to the target
    we can divide the target by the length of the array since we sum each element up
    however this is the best case we may not always get this

Algorithm:
Sort the array A in decreasing order
We try to make all values in A to be the min(A) (the last element)
    If target >= min(arr) * len(arr), we havent hit our target yet
    we should continue to try a value bigger
    So we pop the min(A) value
    we can remove it from target by target -= A.pop()
We continue until the next number is too big for target

In the case that we used up all the elements
    return the max

ex. arr = [4,9,3], target = 10

[9,4,3]
target >= 3 * 3
target -= 3

target = 7
target < 4 * 2

we can have a tie
target / len(arr) - target // len(arr)
7 / 2 - 7 // 2 = .5
3 is the first element which is exactly what we are looking for but what happens when the first element isnt what we want


ex. arr = [2,3,5], target = 10

[5,3,2]
target >= min(arr) * len(arr)
10 >= 2 * 3
target -= 2

target = 8
8 >= 3 * 2
target -= 3

target = 5
target == 5 * 1
if something is greater than or equal to the max value that is our answer, in this case the array will be empty

O(NlogN) time complexity where N is the length of the given array since we sort the array in reverse order.
O(1) space complexity since we just use the given array.
"""

class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        
        arr.sort(reverse = True)
        maxA = arr[0]
        
        while arr and target >= arr[-1] * len(arr):
            target -= arr.pop()
            
        
        if not arr:  # Used all values to be close to `target`.
            return maxA
        if (target / len(arr)) - (target // len(arr)) <= 0.5:  # Fractional part is <= 0.5
            return target // len(arr) # Select the smaller one especially when there's two candidates (== 0.5)
        else:
            return target // len(arr) + 1    
