class MinStack:
    # Create stack to store the differences and update the min
    def __init__(self):
        self.stack = []
        self.min_val = float('inf')

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min_val = val
        else:
            self.stack.append(val - self.min_val)
            self.min_val = min(self.min_val, val)

    def pop(self) -> None:
        dif = self.stack.pop()
        if dif < 0:
            self.min_val = self.min_val - dif

    def top(self) -> int:
        return self.min_val + self.stack[-1] if self.stack[-1] > 0 else self.min_val


    def getMin(self) -> int:
        return self.min_val
