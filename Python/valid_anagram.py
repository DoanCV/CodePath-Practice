class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        to be an anagram, the characters of each string must have the same frequency
        
        keep track of the character frequencies with a hashmap for each string
        
        compare the two hashmaps
        """
        
        # if the length of the two strings are not the same return false
        if len(s) != len(t):
            return False
        
        # get the frequencies
        s_dict = {}
        for i in range(len(s)):
            if s[i] not in s_dict:
                s_dict[s[i]] = 0
            s_dict[s[i]] += 1
        
        t_dict = {}
        for i in range(len(t)):
            if t[i] not in t_dict:
                t_dict[t[i]] = 0
            t_dict[t[i]] += 1
        
        # compare the two frequency counts
        for curr in s_dict:
            if curr not in t_dict:
                return False
            if s_dict[curr] != t_dict[curr]:
                return False
        
        return True

# O(N) time complexity, where N is the length of the given strings, since we traverse with a single loop to get the frequencies and then loop through a hashmap to compare the frequencies.
# O(N) space complexity since we are using two dictionaries and in the worst case all of the characters in the string are unique.
