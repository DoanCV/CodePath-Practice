"""
We are given an array of tasks where each letter represents a different task. They can be done in any order and each one is done in one unit of time
    However, there is a non negative integer n that represents the cooldown period between two of the same tasks so there must be at least n units between them
    Tasks are all capital letters from A to Z

Return the least number of units of times that the CPU will take to finish all the given tasks


M
We could use a heap to start with the most frequently occuring task
    but since our task space is limited to captial letters we can just use an array of size 26 in the worst case


P
Get the frequency of tasks
    we can use a list where each index maps to a capital letter
    sort in ascending order
Find the max amount of idle space that we can have
    = (max Frequency task - 1) * n
    Iterate and reduce the idle space count


R
ex. ["A","A","A","B","B","C"] cooling time n = 2

frequencies = [3,2,1]
sort
frequencies = [1,2,3]

spaces = (3 - 1) * 2 = 4

[A, idle, idle, A, idle, idle, A]
[A, B, idle, A, B, idle, A]
[A, B, C, A, B, idle, A]

idle spaces = 1
len(tasks) = 6 + 1 = 7 
    equal to length of [A, B, C, A, B, idle, A]
"""
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        if len(tasks) == 0:
            return 0
        
        frequencies = [0 for _ in range(26)]
        for char in tasks:
            frequencies[ord(char) - ord("A")] += 1
        
        frequencies.sort()
        max_freq = frequencies[25] - 1
        spaces = max_freq * n
        for i in range(24, -1, -1):
            spaces -= min(frequencies[i], max_freq)
        
        # spaces can be negative so we have to handle that
        spaces = max(0, spaces)
        return spaces + len(tasks)
