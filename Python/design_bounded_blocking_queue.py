"""
Implement a thread safe bounded blocking queue that has the following methods:
  - Constructor intializes the queue with a maximum capacity
  - Enqueue() adds and element to the front of the queue. If the queue is full, the calling thread is blocked until the queue is no longer full
  - Dequeue() returns the element at the rear of the queue and removes it. If the queue is empty, the calling thread is blocked until the queue is no longer empty
  - Size() returns the number of elements currently in the queue 
  
bounded means there is a capacity
to implement a thread safe queue

constructor
  the size
  the queue
  locks on each method apart from size
  acquire a blocking lock
"""
from collections import deque
from threads import Lock
class BoundedBlockingQueue(object):
  
  def __init__(self, capacity: int):
    # initialize the locks
    self.enqueueLock = Lock()
    self.dequeueLock = Lock()
    
    self.queue = deque()
    self.capacity = capacity
    
    # we first create the queue so it is empty, lock dequeue
    self.dequeueLock.acquire()
    
  def enqueue(self, element: int) -> None:
    self.enqueueLock.acquire()
    self.queue.append(element)
    
    # we can append to our queue since we are not at capacity
    if self.size() < self.capacity:
      self.enqueueLock.release()
    
    # we can pop from our queue since we just added an element, this is especially important if the queue is at capacity
    if self.dequeueLock.locked():
      self.dequeueLock.release()
    
  def dequeue(self) -> int:
    self.dequeueLock.acquire()
    bottom = self.queue.popleft()
    
    # we can pop if our queue is still not empty
    if self.size() > 0:
      self.dequeueLock.release()
    
    # we popped an element so we can't be at capacity so we can enqueue if we want
    if self.enqueueLock.locked():
      self.enqueueLock.release()
    
    return bottom
  
  def size(self) -> int:
    return len(self.queue)
