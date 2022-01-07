class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        if not nums:
            return []
        
        result = [0 for _ in range(len(nums))]
        
        def divide(tuples):
            
            if len(tuples) == 1:
                return tuples
            
            mid = len(tuples) // 2
            left = divide(tuples[:mid])
            right = divide(tuples[mid:])
            
            return conquer(left, right)
            
        def conquer(left, right):
            
            arr = []
            i = 0
            j = 0
            while i < len(left) and j < len(right):
                if left[i][0] > right[j][0]:
                    
                    result[left[i][1]] += len(right) - j # the number of elements that are smaller on the right is the jump gap
                    
                    arr.append(left[i])
                    i += 1
                
                else:
                    arr.append(right[j])
                    j += 1
            
            arr.extend(left[i:] or right[j:]) # add the remaining elements
            return arr
        
        # (index, value) pairs. The value is used for the sorting and the index is used for tracking the jumps
        tuples = [(value, index) for index, value in enumerate(nums)]
        divide(tuples)
        
        return result
