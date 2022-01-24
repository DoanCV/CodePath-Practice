"""
Optimal solution, better than heap
    use two hashmaps
    the first maps the word to its frequency
    then we build the second one which maps the frequency to a list of words of that frequency
   
find the maximum frequency
starting from the max frequency add the words in the list to the result until we have k of them
    k can be negative so return the remainder
    decrement the max frequency when we finish all the words since we may need to keep going
"""
from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        freq_map = Counter(words)
        word_map = {}
        
        max_freq = 0 
        for key, value in freq_map.items():

            if value not in word_map:
                word_map[value] = []
                
            word_map[value].append(key)
            max_freq = max(max_freq, value)
            
        
        result = []
        temp = k
        while k > 0:
            
            if max_freq in word_map:
                
                words = sorted(word_map[max_freq])
                
                k -= len(words)
                
                if k < 0:
                    for i in range(temp - len(result)):
                        result.append(words[i])
                    
                else:
                    for word in words:
                        result.append(word)
                
            max_freq -= 1
        
        return result

# O(N) time complexity since we solve in worst case three passes.




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

# O(NlogN) time complexity, where N is the length of the given array, since we have to traverse the given array once to get the frequencies. The other traversals are worst case O(N) since we can have an array of all unique words. But N + N grows asymptotically as N. When we add to the heap that takes log(N) time. 
# O(N) space complexity since in the worst case the given array has only unique words which means the length of the array is the same length of the hashmap. The size of the heap is the same as the hashmap.
