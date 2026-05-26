class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        if not self.stack:
            minNum = val
        else:
            minNum = min(val, self.stack[-1][1])
        
        self.stack.append((val, minNum))

    

    def pop(self) -> None:
        return self.stack.pop()[0]
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]
        
