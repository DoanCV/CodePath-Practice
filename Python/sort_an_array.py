"""
Obviously do not just use .sort()

algorithms:
    bubble sort, even Obama says its slow. essentially we find pairs that are out of order and we swap them, keep doing this until the array is sorted
        O(N^2)
    selection sort, find the minimum, remove it and add it to output list, keep going until the original array is empty

lets implement quick sort
    issue: if already sorted and our pivot is at the end of the subarray then we get TLE
    issue: random pivot may not always work in our favor

solution is to just use merge sort, see below the docstring

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        self.quick_sort(nums, 0, len(nums) - 1)
        
        return nums
    
    def quick_sort(self, nums, left, right):
        
        if left >= right:
            return
            
        pivot = self.parition(nums, left, right)

        self.quick_sort(nums, left, pivot - 1)
        self.quick_sort(nums, pivot + 1, right)
    
    
    def parition(self, nums, left, right):
        
        start = left
        pivot = right
        
        while left <= right:
            if nums[left] < nums[pivot]:
                nums[left], nums[start] = nums[start], nums[left]
                start += 1
            left += 1
        
        nums[start], nums[pivot] = nums[pivot], nums[start]
        
        return start
"""

# Alright merge sort, python uses modified merge sort so I have to implement it to earn the right to use it
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        self.merge_sort(nums)
        
        return nums
    
    def merge_sort(self, nums):
        
        # check if already not sorted
        if len(nums) > 1:
        
            # split into two subproblems
            mid = len(nums) // 2
            
            left_half = nums[:mid]
            right_half = nums[mid:]

            self.merge_sort(left_half)
            self.merge_sort(right_half)
            
            self.merge(nums, left_half, right_half)

    def merge(self, nums, left_half, right_half):
        lptr = 0
        rptr = 0
        k = 0
        
        while lptr < len(left_half) and rptr < len(right_half):
            if left_half[lptr] < right_half[rptr]:
                nums[k] = left_half[lptr]
                lptr += 1
            else:
                nums[k] = right_half[rptr]
                rptr += 1
                
            k += 1
        
        # add the rest
        while lptr < len(left_half):
            nums[k] = left_half[lptr]
            lptr += 1
            k += 1
        
        while rptr < len(right_half):
            nums[k] = right_half[rptr]
            rptr += 1
            k += 1
        
# O(NlogN) time complexity where N is the length of the given array. Best case our array is length 1 so that is constant. Hoever in the worst case, we are cutting our searches in half. We have a recurrance relation T(N) = 2T(N/2) + N. By the Master Theorem, we evaluate our f(N), which is N and mulitply by logN.        
