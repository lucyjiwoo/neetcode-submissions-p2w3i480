class MinStack:
    def __init__(self):
        self.stack = []
        self.minhis = []
        self.min = None
    def push(self, val: int) -> None:
        
        if not self.stack:
            self.min = val
        elif self.min > val:
            self.min = val

        self.minhis+= [self.min]
        self.stack += [val]

    def pop(self) -> None:
        if not self.stack or len(self.stack) == 1:
            self.stack = []
            self.minhis = []
            self.min = None
        if self.stack:
            m = len(self.stack)
            self.minhis = self.minhis[:m-1]
            if self.stack[m-1] == self.min:
                self.min = self.minhis[m-2]
            self.minhis = self.minhis[:m-1]
            self.stack = self.stack[:m-1]
    def top(self) -> int:
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int:
        return self.min