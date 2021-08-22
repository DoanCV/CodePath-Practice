class movingAverage:
  
  def __init__(self, windowSize):
    self.size = windowSize
    self.array = []
    self.curr_sum = 0
  
  def next(self, val):
    self.array.append(val)
    self.curr_sum += val
    
    if len(self.array) > self.size:
      self.curr_sum -= self.array.pop(0)
    
    return self.curr_sum / self.size
