class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        # convert string to list since string is immutable
        list_palindrome = list(palindrome)
        
        # two pointer
            # find the first non "a"
                # change it
        left = 0
        right = len(list_palindrome) - 1
        while left < right:
            if list_palindrome[left] != 'a':
                list_palindrome[left] = 'a'
                return "".join(list_palindrome)
            
            left += 1
            right -= 1
        
        # catch edge cases
            
        # length 1 strings are palindromes since they are 1 character
            # return an empty string
        if len(list_palindrome) == 1:
            return ""
        
        # if every character is an a then we need to change the last character to a b
        list_palindrome[-1] = "b"
        return "".join(list_palindrome)
