from collections import defaultdict
class AutocompleteSystem:
  def __init__(self, sentences, times):
    self.search = ""
    
    self.history = defaultdict(int)
    for i in range(len(sentences)):
      self.history[sentences[i]] = times[i]

    self.matches = []

  def input(self, c):
    # end of search when we see "#" so then we will save search to history and reset
    if c == "#":
      self.history[self.search] += 1
      self.search = ""
      self.matches = []
      return
    
    # if we just started a search then we need to populate the matches array with the potential candidates
    if not self.search:
      for sentence in self.history:
        if sentence[0] == c:
          self.matches.append([sentence, self.history[sentence]])

      # sort candidates byt frequency in descending order then ascending by ASCII
      self.matches.sort(key = lambda x: (-x[1], x[0]))
      self.matches = [x[0] for x in self.matches]
    
    # we already have a search going on
    else:
      index = len(self.search)
      self.matches = [match for match in self.matches if len(match) > index and match[index] == c] # we need to check if the index we are comparing is within the length of the current key in history

    self.search += c
    return self.matches[:3] # return top 3
