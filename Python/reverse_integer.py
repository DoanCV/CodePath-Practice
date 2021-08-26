"""
Terrible problem, this is useless but...
@CSHomies Regardless, lets get cracking :kekW:

two thoughts/approaches
    1. convert to string and then let python do the work with splicing
        if splicing is not allowed we will convert to array and use two pointer since string is immutable
    2. modulo the given integer by 10 and add it, then multiply by 10 to move the digit up a place
"""

class Solution:
    def reverse(self, x: int) -> int:
        """
        # method 1
        
        x = str(x)
        
        add_negative_sign_in_the_end = False
        if x[0] == "-":
            add_negative_sign_in_the_end = True
            x = x[1:]

        max_int = 2**31 - 1
        
        x = x[::-1]
        
        if max_int < float(x):
            return 0
        
        if add_negative_sign_in_the_end:
            return int("-" + x)
        else:
            return int(x)
            
        """
        
        # method 2
        
        num_reversed = 0
        num = abs(x)
        
        while num:
            num_reversed = num_reversed * 10 + num % 10
            num = num // 10
        
        if abs(x) != x:
            num_reversed = -num_reversed
        
        max_int = 2**31 - 1
        if num_reversed < max_int and num_reversed> -max_int:
            return num_reversed    
        else:
            return 0
        
