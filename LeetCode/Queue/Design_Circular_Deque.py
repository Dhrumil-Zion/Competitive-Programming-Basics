class MyCircularDeque:

    def __init__(self, k):
        self.CircularDeque = []
        self.k = k
        
        
    def insertFront(self, value):
        if len(self.CircularDeque) < self.k:
            self.CircularDeque = [value] + self.CircularDeque
            print(self.CircularDeque)
        print("error")
        

    def insertLast(self, value):
        if len(self.CircularDeque) < self.k:
            self.CircularDeque = self.CircularDeque + [value]
            print(self.CircularDeque)
        print("error")
        

    def deleteFront(self):
        if self.CircularDeque:
            self.CircularDeque.pop(0)
            print(self.CircularDeque)
        print("error")
        
    def deleteLast(self):
        if self.CircularDeque:
            self.CircularDeque.pop()
            print(self.CircularDeque)
        print("error")
        

    def getFront(self):
        if self.CircularDeque:
            print(self.CircularDeque[0])
        print("error")
        
    def getRear(self):
        if self.CircularDeque:
            print(self.CircularDeque[-1])
        print("error")
        

    def isEmpty(self):
        print(not self.CircularDeque)
		

    def isFull(self):
        print(len(self.CircularDeque) == self.k)
        

k=3
value = [1,4]
obj = MyCircularDeque(k)
param_1 = obj.insertFront(value[0])
param_2 = obj.insertLast(value[1])
param_3 = obj.deleteFront()
param_4 = obj.deleteLast()
param_5 = obj.getFront()
param_6 = obj.getRear()
param_7 = obj.isEmpty()
param_8 = obj.isFull()