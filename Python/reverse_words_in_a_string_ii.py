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
