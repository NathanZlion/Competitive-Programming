class MyCircularDeque:

    def __init__(self, k: int):
        self.deq = deque([])
        self.size = k

    def insertFront(self, value: int) -> bool:
        print(self.deq)
        if self.isFull():
            return False
        self.deq.appendleft(value)
        print(self.deq)

        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False        
        self.deq.append(value)
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.deq.popleft()
        return True        

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.deq.pop()
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.deq[0]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.deq[-1]


    def isEmpty(self) -> bool:
        return len(self.deq) == 0
        

    def isFull(self) -> bool:
        return len(self.deq) == self.size
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()