class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        traverse backwards since that is inline with how I add normally
        mod the current sum by 10 for the new place value
        integer divide for the carry
        if the final carry after the original length of the array is not 0, insert it at the start of the list
        """
        
        # use to add 1
        carry = 1
        
        for i in range(len(digits) - 1, -1 , -1):
            total = carry + digits[i]
            
            # update current digit
            digits[i] = total % 10
            
            # update the carry to add to the next digit
            carry = total // 10
        
        # if there is still a carry after the highest place insert the carry at the front
        if carry > 0:
            digits.insert(0, carry)
        
        return digits

# O(N) time complexity, where N is the length of the given array, since we traverse the array once.
# O(1) space complexity since we not using any new data structures and solve in-place.
