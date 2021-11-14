"""
we have two arrays, each are sorted in non decreasing order
    if we were to combine the two arrays find the median

constraint: O(log(m+n)) time complexity
    actually merging the two arrays takes O(n+m) time so we can't do this

the median in odd length is middle element
    in even length it is the average of the two values in the middle

without combining the two given arrays, we can find our midpoint that gets us a left and right sides

ex to show even case
nums1 = [1,2,3,4,5,6,7,8]
nums2 = [1,2,3,4]

even length case
12 elements in total we still split into two groups, left and right
    [1,2,3,4] say our left side has 1,2 that means right is 3,4
    this also means that in our other array we have half - left elements in the left half
        half is 6 since 12/2 = 6 but we also have to round down when odd number of elements
    [1,2,3,4] from [1,2,3,4,5,6,7,8]
    
    now we check is our left partition in one array less than the right partition in the other array and vice versa?
        if so we can find our median from the position of our midpoints
        else we have to continue with binary search
            keep in mind we only have two pointers, both of which are in one array since we can fo half - left to find out where in the other array we need to look
        
    in this example
    [1,2,3,4,5,6,7,8]
           ^       
           
    [1,2,3,4]
     l m   r
    
    4 is not less than or equal to 3 so we need to move our pointers
        in this case we move left to m + 1
    now our mid is
    [1,2,3,4,5,6,7,8]
         ^ 6 - 3 = size 3 partition      
           
    [1, 2, 3, 4]
          l/m r
    
    this is valid since 3 from nums1 is less than 4 from nums2 and 3 from nums2 is less than 4 from nums2
    once we have the partition we need to find the median
    take the maximum of the left parititon and the minimum of the right partition and then take the average of the two

odd length case
    same idea until when we find the correct partition
    we pick the minimum of the right partitions
    
edge case
    if we have absolute minimums in one then it will always be less than or equal to everything else so we need something beyond our constraints, use -inf and inf
    
O(log(min(m,n)) time complexity since we running binary search on the smaller array.
"""

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        total_length = len(nums1) + len(nums2)
        half_length = total_length // 2
        
        # in the examples above I search on nums2 since it was smaller, lets swap them if that is the case here
        # if nums1 is smaller swap
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
            
            
        left = 0
        right = len(nums2) - 1
        # we are guranteed a median so we can break when we find the answer
        while True:
            i = (left + right) // 2 # index of mid point in nums2
            j = half_length - i - 2 # index of mid point in nums1, verify by example but we know that we are 0-indexing
            
            # check if we have the correct partition
            # keep in mind we can also go out of bounds so if we have gone out then give default values, left -> -inf and right -> inf
                # this is safe since odd case we return minimum of rights which is less than inf
                # in the even case we use the maximum of the left so everything is greater than -inf
            nums2_left = nums2[i] if i >= 0 else float("-inf")
            nums2_right = nums2[i + 1] if (i + 1) < len(nums2) else float("inf")
            
            nums1_left = nums1[j] if j >= 0 else float("-inf")
            nums1_right = nums1[j + 1] if (j + 1) < len(nums1) else float("inf")
            
            
            if nums2_left <= nums1_right and nums1_left <= nums2_right:
                # we have the valid partition, now handle odd/even cases
                if total_length % 2 == 1:
                    return min(nums2_right, nums1_right)
                else:
                    return (max(nums2_left, nums1_left) + min(nums2_right, nums1_right)) / 2
            
            # we are not done, handle the two cases
            elif nums2_left > nums1_right: # we have too many elements from nums2, move right pointer
                right = i - 1
            else:
                left = i + 1
