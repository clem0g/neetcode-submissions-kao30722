class MinStack:

    def __init__(self):
       self.stack = []


    def push(self, val: int) -> None:
        x = self.stack 
        x.append(val)

    def pop(self) -> None:
        x = self.stack 
        x.pop()

    def top(self) -> int:
        x = self.stack  
        return x[-1]

    def getMin(self) -> int:
        x = self.stack  
        return min(x)
