from queue import PriorityQueue
from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        """
        Use a hashmap to get the frequencies of each word
        Use priority queue to insert the word and its frequency where the priority is the frequency
        
        for the hashmap, Counter from collections is great since it initalizes all values to 0 so I do not need if statement
        instead of heapq, PriorityQueue is thread-safe
        """
        
        heap = PriorityQueue()
        frequencies = Counter()
        
        # Get the frequencies
        for word in words:
            frequencies[word] += 1
        
        # Add tuples into the priority queue. We are storing the frequency and the corresponding word. The priority comes first when inserting into the priority queue.
        # There is a negative sign before the frequency since .get() pops the minimum priority first so the negative sign will force the queue to get the highest magnitude counts first.
        for word in frequencies:
            freq = frequencies[word]
            heap.put( (-freq, word) )
        
        result = []
        for _ in range(k):
            curr = heap.get()
            result.append( curr[1] )
        
        return result

# O(N) time complexity, where N is the length of the given array, since we have to traverse the given array once to get the frequencies. The other traversals are worst case O(N) since we can have an array of all unique words. But N + N + N grows asymptotically as N.
# O(N) space complexity since in the worst case the given array has only unique words which means the length of the array is the same length of the hashmap. The size of the heap is the same as the hashmap.
