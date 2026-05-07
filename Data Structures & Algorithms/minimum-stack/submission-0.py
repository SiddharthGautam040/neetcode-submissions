class MinStack:

    def __init__(self):
        self.arr = []
        self.min_stack = []
        

    def push(self, val: int) -> None:
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(self.min_stack[-1], val))
        self.arr.append(val)
        return None

    def pop(self) -> None:
        self.arr.pop()
        self.min_stack.pop()
        return None

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
