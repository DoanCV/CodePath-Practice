"""
all our letters are lowercase

We can use BFS
    each level in our graph is a one letter change
    we can keep track of the word and the depth that we find the word
    we can also use a set to quickly keep unqiue words in our wordlist and quickly find them
    
    the end word has to be in the given wordlist otherwise there is no answer

when we find the endword then we are done and return the depth that we had to go in order to find the word
find all one letter change varatations and check if it is in our wordlist
    change each letter in our current word with eveyr letter in the alphabet
    if a variation is in the wordlist add it to our queue and count that as taking another transformation
    if 
"""

from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        
        queue = deque()
        queue.append( (beginWord, 1) )
        
        while queue:
            
            currWord, stepsTaken = queue.popleft()
            
            if currWord == endWord:
                return stepsTaken
            
            for letter_pos in range(len(currWord)):
                for char in alphabet:
                    
                    transformed = currWord[:letter_pos] + char + currWord[letter_pos + 1:]
                    
                    if transformed in wordList:
                        # if we do not remove the word then we will come back to it later and get stuck
                        wordList.remove(transformed)
                        queue.append( (transformed, stepsTaken + 1) )
        
        return 0
