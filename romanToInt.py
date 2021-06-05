class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        """
        1-3999
        
        ex:
        MMMCMXCIX => 3999:
            MMM + CM + XC + IX
            3000 + 900 + 90 + 9
        
            M + M + M + CM + XC + IX
            1000 + 1000 + 1000 + 900 + 90 + 9
        
        store all cases in hash table
        look for substrings to account for all cases given
            either one char or two char
                one normal just add
                two, special case just add as well
        
        keep track of:
        current index
        integer result
        
        logic:
        start from the left
        while index is less than the length of the string
            if the char at the current index and next index are speical case AND (the comment below)
            # at the end of the string peeking ahead is invalid operation so check if the current index + 1 is less than the length of given string
                then add that to the sum
                skip two indicies and move on to the next iteration
            else
                add current match in hash table to sum
                increment indexs by 1
            
        
        """
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        
        current = 0
        integer_result = 0
        while current < len(s):
            if s[current:current+2] in roman and current + 1 < len(s):
                integer_result += roman[s[current:current+2]]
                current += 2
            else:
                integer_result += roman[s[current]]
                current += 1
        return integer_result
