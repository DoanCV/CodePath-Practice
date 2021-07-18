import queue
"""
queue class methods:
- qsize()
    returns size
- put()
    pushes into queue
- get()
    pops and returns popped element

we can't reverse when queue is empty or when k is less than 1 or when k is greater than the size of the given queue
  we can just return the given queue

we can pop the first k and push it into a stack
then we pop the stack and push the elements into the original queue k times to empty the temporary stack (this is the reversing)
with the size and k pop and push the rest of the original queue that was untouched
"""
def reverse_first_k(q,k):
  if q.qsize() < k or k < 1 or q.qsize() == 0:
    return q
  
  temp = []
  i = 0
  while i < k:
    temp.append( q.get() )
    i += 1
  
  while len(temp) > 0:
    q.put( temp.pop() )
  
  i = 0
  while i < q.qsize() - k:
    q.put( q.get() )
    i += 1
  
  return q

# O(N) time complexity, where N is the size of the given queue.
# O(N) space complexity since in the worst case k is the size of the given queue so the temporary stack is the same size.
