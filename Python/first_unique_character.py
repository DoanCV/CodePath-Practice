class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        store the frequency of the characters in a hashmap
        loop through the string again but if the value at the current character is 1 return the index
        return -1 if there is no such character
        """
        
        # insert into hashmap
        dict = {}
        for i in range(len(s)):
            if s[i] not in dict:
                dict[s[i]] = 0
            dict[s[i]] += 1
            
        for i in range(len(s)):
            if dict[s[i]] == 1:
                return i 
        
        return -1
      
# O(N) time complexity, where N is the length of the given string, since we are traversing through the given string with single for loops. We do this two times separately which is still linear.
# O(N) space complexity since we are using a hashmap to store the frequencies of the characters. In the worst case, the size of the frequency is N since there are only unique characters.
