from queue import PriorityQueue
from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        """
        Use a hashmap to get the frequencies of each word
        Use priority queue to insert the word and its frequency where the priority is the frequency
        """
        
        heap = PriorityQueue()
        frequencies = Counter()
        
        for word in words:
            frequencies[word] += 1
        
        for word in frequencies:
            freq = frequencies[word]
            heap.put( (-freq, word) )
        
        result = []
        for _ in range(k):
            curr = heap.get()
            result.append( curr[1] )
        
        return result
