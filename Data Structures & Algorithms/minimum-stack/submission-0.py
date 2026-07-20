class MinStack:

    def __init__(self):
        self.stack = []
        
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        

    def pop(self) -> None:
        if not self.stack:
            raise IndexError("pop from empty stack")
        self.stack.pop()
        

    def top(self) -> int:
        if not self.stack:
            raise IndexError("top from empty stack")
        return self.stack[-1]

        

    def getMin(self) -> int:
        if not self.stack:
            raise IndexError("getMin from empty stack")
        minimum = self.stack[0]

        for val in self.stack:

            if val < minimum:
                minimum = val


        return minimum
            
        
