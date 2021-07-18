class Solution:
    def reverseWords(self, s: str) -> str:
        """
        two pointers
        each pointer is pointing to a word and we just swap and increment both
        to get the entire word, we split on white space since strings are immutable
        """
        
        # split on whitespace
        arr = s.split()
        
        # initalize the two pointers
        left = 0
        right = len(arr) - 1
        
        # while the left pointer does not cross the right pointer
        while left < right:
            
            # swap the elements of the array
            arr[left], arr[right] = arr[right], arr[left]
            # increment left and decrement right
            left += 1
            right -= 1
            
        # return as joined string
        return " ".join(arr)

# O(N) time complexity, where N is the number of given words, since we are traversing through the words once in N/2 steps. N/2 grows asymptocially as N.
# O(N) space complexity since we are using split to move all the words into an array.
