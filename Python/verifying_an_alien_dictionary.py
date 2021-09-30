"""
Store the position of the letter in a hashmap since this how we will know the order
    hashamp = {letter: position in the given string(order)}


convert each word to its ordering
    
then compare the ordering of each word
"""

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        # interpret and store the alien ordering
        ordering = {}
        for position, value in enumerate(order):
            ordering[value] = position
            
        # covert the words based on the ordering
        new_words = []
        for word in words:
            converted = []
            
            for char in word:
                converted.append(ordering[char])
            
            new_words.append(converted)
            
        """
        # parallel traversal since nested for loop doesnt exactly work
        for word1, word2 in zip(new_words, new_words[1:]):
            # > since we may have duplicates
            if word1 > word2:
                return False
        """
        
        for i in range(1, len(new_words)):
            
            if new_words[i - 1] > new_words[i]:
                return False
            
        
        
        # everything is sorted as we have checked
        return True
        
