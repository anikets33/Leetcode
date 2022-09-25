class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.length = 0
        self.queue = [0]*k
        self.front = -1
        self.rear = -1

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.front = (self.front+1)%self.size
        self.rear = (self.rear+1)%self.size
        self.queue[self.rear] = value
        self.length += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        if self.length == 1:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front+1)%self.size
        self.length -= 1
        return True

    def Front(self) -> int:
        return self.queue[self.front] if self.front != -1 else self.front

    def Rear(self) -> int:
        print(self.queue)
        return self.queue[self.rear] if self.rear != -1 else self.rear

    def isEmpty(self) -> bool:
        return self.length == 0

    def isFull(self) -> bool:
        return self.length == self.size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
