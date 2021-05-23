class MyCircularQueue:
    def __init__(self, k: int):
        self.data = [0] * k
        self.maxSize = k
        self.head = 0
        self.tail = -1  
    def enQueue(self, val: int) -> bool:
        if self.isFull(): return False
        self.tail = (self.tail + 1) % self.maxSize
        self.data[self.tail] = val
        print(self.data)
    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        if self.head == self.tail: self.head, self.tail = 0, -1
        else: self.head = (self.head + 1) % self.maxSize
        print(self.data)
    def Front(self) -> int:
        return -1 if self.isEmpty() else self.data[self.head]
    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.data[self.tail]
    def isEmpty(self) -> bool:
        return self.tail == -1
    def isFull(self) -> bool:
        return not self.isEmpty() and (self.tail + 1) % self.maxSize == self.head

myCircularQueue = MyCircularQueue(3)
myCircularQueue.enQueue(1) 
myCircularQueue.enQueue(2) 
myCircularQueue.enQueue(3) 
myCircularQueue.enQueue(4)
myCircularQueue.Rear()    
myCircularQueue.isFull()  
myCircularQueue.deQueue()  
myCircularQueue.enQueue(4) 
myCircularQueue.Rear()     