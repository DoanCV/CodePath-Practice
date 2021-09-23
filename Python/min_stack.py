class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.stack.append( (val, val) )
        else:
            top_val, local_min = self.stack[-1]
            if local_min < val:
                self.stack.append( (val, local_min) )
            else:
                self.stack.append( (val, val) )

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        top_val, local_min = self.stack[-1]
        return top_val

    def getMin(self) -> int:
        top_val, local_min = self.stack[-1]
        return local_min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
