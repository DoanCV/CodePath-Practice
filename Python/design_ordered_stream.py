class OrderedStream:

    def __init__(self, n: int):
        self.data_stream = [None for _ in range(n)]
        self.pointer = 0

    def insert(self, idKey: int, value: str):
        self.data_stream[idKey - 1] = value
        
        # case 1, we inserted something past the pointer
        if idKey - 1 > self.pointer:
            return []
        
        # case 2, we inserted at the pointer now return the chunk if the there is a value other than None
        while self.pointer < len(self.data_stream) and self.data_stream[self.pointer] is not None:
            self.pointer += 1
        
        return self.data_stream[idKey - 1: self.pointer]

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
