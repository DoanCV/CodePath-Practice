"""
# remove whitespace
    use .strip()
# check for sign, positive is implicit (sometimes), negative is always explicit 
# keep numbers within 32bit integer range

# process the string -> int
    # assume I am allowed to use int()

"42" => 40 + 2
result = 0

i = 0
result = 4
# multiply result by 10 add curr number % 10

i = 1
result = 42

"""

class Solution:
    def myAtoi(self, s: str) -> int:
        
        # remove whitespace
        s = s.strip()
        
        # case 0: empty string
        if len(s) == 0:
            return 0
        
        # process the sign
        if s[0] == "-":
            sign = -1
        else:
            sign = 1
        
        # find start position of the integer as a string
        if s[0] in ["-", "+"]:
            i = 1
        else:
            i = 0
        
        result = 0
        # while we are not at the end of the string and we have a digit
        while i < len(s) and s[i].isdigit():
            result = result * 10 + int(s[i]) % 10
            i += 1
        
        # restrict result to the given bounds of 32 bit integer
        result = sign * result
        if result > 2**31 - 1:
            result = 2**31 - 1
        if result < -2**31:
            result = -2**31
        
        # return result
        return result
