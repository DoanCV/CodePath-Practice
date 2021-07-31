class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        
        if a == 0:
            return b
        if b == 0:
            return a
        
        mask = 0xffffffff
        
        while b:
            sum = (a ^ b) & mask
            carry = ((a & b) << 1) & mask
            a = sum
            b = carry
        
        if (a >> 31) & 1:
            return ~(a ^ mask)
        # 11111111 mask
        # 10101010 a
        # 01010101 a ^ mask
        # 10101010 ~(a ^ mask)
        
        return a
      
# O(1) time complexity since we are limited by 32 bit ints. There can be 0s to the left but we still have to read them.
# O(1) space complexity since we are not using any extra data structures.
