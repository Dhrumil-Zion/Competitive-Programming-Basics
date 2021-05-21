class CustomStack:
    stack = []
    len_stack = 0
    def __init__(self, maxSize: int):
        self.stack = []
        self.size = maxSize 

    def push(self, x: int) -> None:
        if len(self.stack) < self.size:
            self.stack.append(x)

    def pop(self) -> int:
        if self.stack:
            return self.stack.pop()
        else:
            return -1
        

    def increment(self, k: int, val: int) -> None:
        for i,j in enumerate(self.stack[:k]):
            self.stack[i] += val
            
# ["CustomStack","push","push","pop","push","push","push","increment","increment","pop","pop","pop","pop"]
# [[3],[1],[2],[],[2],[3],[4],[5,100],[2,100],[],[],[],[]]
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)