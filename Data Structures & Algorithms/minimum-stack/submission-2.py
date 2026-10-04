class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float("inf")
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val < self.min:
            self.min = val
        

    def pop(self) -> None:
        popped = self.stack.pop()
        if popped == self.min:
            if self.stack:
                self.min = min(self.stack)
            else:
                self.min = float("inf")

        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min
        
