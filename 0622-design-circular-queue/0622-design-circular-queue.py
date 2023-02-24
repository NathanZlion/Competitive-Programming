class MyCircularQueue:
    def __init__(self, k: int):
        self.queue = []
        self.size = k
        self.head = 0        

    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            self.queue.append(value)
            return True
        return False            

    def deQueue(self) -> bool:
        if self.head < len(self.queue):
            self.head += 1
            return True
        return False

    def Front(self) -> int:
        if not self.isEmpty():
            return self.queue[self.head]
        return -1

    def Rear(self) -> int:
        if not self.isEmpty():
            return self.queue[-1]
        return -1

    def isEmpty(self) -> bool:
        return len(self.queue) == self.head

    def isFull(self) -> bool:
        return len(self.queue) - self.head == self.size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()