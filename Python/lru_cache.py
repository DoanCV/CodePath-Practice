class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        self.head = Node(0, 0)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def get(self, key: int) -> int:
        # if key exists return the value
            # make the one we just accessed the most recently used one
            # move it to the head
            
        # return -1 if the key does not exist

    def put(self, key: int, value: int) -> None:
        # add to hashmap and head of linkedlist
        
        # if the size is greater than capacity, remove the tail 
    
    
    # at initialization
    # head <-> tail
    # add node say 1
    # head [1] tail
    def addToHead(self, node):
        # head <-> [1]  tail
        headNext = self.head.next
        self.head.next = node
        node.prev = self.head
        
        # head <-> [1] <-> tail
        node.next = headNext
        headNext.prev = node
    
    # say capacity is 0, we want to remove the node we just added
    # head <-> [1] <-> tail
    def removeFromList(self, node):
        nextNode = node.next
        prevNode = node.prev
        
        # head <- [1] -> tail
        # head <-> tail
        prevNode.next = nextNode
        nextNode.prev = prevNode
        
    def removeEndofList(self):
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

"""
We have to keep track of two things, the key-value pair and something to keep track of when we accessed it relative to the other pairs

We also want O(1) time complexity for our two operations

the data structure that has the time complexity that we need for our operations is a hashmap
    we will map key to value
    issue: how will we keep track of the "least recently used" part?
    we can add a time stamp to the value so that we are storing enough info
    issue: how will we determine least recently used in constant time? looking up a value is linear since we are trying to figure out the key
    
we can map the key to a node in a singly linkedlist
    the linkedlist head will be the most recently used and the tail will be the least recently used
    issue: using get will mean that we have to change the order of the nodes to reflect most recently used and swapping nodes in singly linkedlist takes linear time since we have to find the node and its previous

we can use a doubly linkedlist to get the previous node to reassign its next node
    that way we can make the node we used get operation the new head
    issue: our put is also our delete when we hit capacity, we do not want users to have to deal with delete logic we have to handle that at capacity
    we will store the key and the value in each node of our linkedlist that way we can access the key of the tail node and delete it from the hashmap and doubly linkedlist
    
"""
