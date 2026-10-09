class MinStack:

    def __init__(self):
        self.stack = []        

    def push(self, val: int) -> None:
        if self.stack:
            cur_min = min(self.stack[-1][1], val)
        else:
            cur_min = val
        
        self.stack.append((val, cur_min))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]
        
