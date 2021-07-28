"""
Reverse the whole array with two pointers
Scan for a word (delimited by space) and reverse each word

if we are at the end we won't detect a space so we will need to reverse the last word as well
"""

def reverse_word(sentence, start, end):
  
  while start < end:
    sentence[start], sentence[end] = sentence[end], sentence[start]
    start += 1
    end -= 1

def reverse_words(sentence):
  if len(sentence) == 0:
    return
   
  reverse_word(sentence, 0, len(sentence))
  
  start = 0
  for i in range(len(sentence)):
    
    if sentence[i] == " " or i == len(message) - 1:
      reverse_word(sentence, start, i - 1)
      front = i + 1
      
  return sentence

# O(N) time complexity, where N is the length of the given array, since we pass through the array twice independently.
# O(1) space complexity since we are required to solve the problem in-place.
