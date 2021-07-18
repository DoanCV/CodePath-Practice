"""
Given an input string, write a function that returns the run-length encoded string for the input string.

For example:

Input: "wwwwaaadexxxxxx"
Output: "w4a3d1e1x6"

"""

def encode(s):
  """
  Since we are keeping track of frequencies we can use a hashmap hten append to a result string. However, that gets the total frequency not consecutive.
  i.e. "wwawwaaadexxxxxx" with the hashmap gives "w4a4d1e1x6" which is incorrect, it should be "w2a1w2a3d1e1x6"
  So if we need it to be consecutive then we need a differnt solution.
  
  Another approach, the one I will use is with two pointers starting at the first element of the string. 
  One pointer will traverse through the string one character at a time until the character changes. 
  I will also keep track of a counter as part of the encoding.
  Once there is a change add the left pointer to the result and the count and move the left pointer to the right pointer and increment the right pointer solution.
  """
  
  # Initialize pointers and result string
  result = ""
  left = 0
  right = 1
  
  # while the left pointer is not at the end of the given string
  for left in range(len(s)):
    
    # initalize count to 1 since this will reset when we get a character change
    counter = 1
    
    # while the letter at the two pointers are the same and the right pointer is not at the end of the string, increment the count and the right pointer
    while s[left] == s[right] and right < len(s):
      counter += 1
      right += 1
    
    # append to result
    result.append(s[i])
    result.append(str(counter))
    
    # move the left pointer to the next letter and increment the right pointer
    left = right
    right += 1
    
  # return the result
  return result

# O(N) time complexity, where N is the length of the given string, since we have to traverse through the string to encode it and here we do it once.
# O(N) space complexity since the result array grows linearly with the length of the given string.
