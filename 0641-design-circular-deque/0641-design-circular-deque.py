class MyCircularDeque:

    def __init__(self, k: int):
        self.deq = deque([])
        self.size = k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.deq.appendleft(value)
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
        return self.deq[0] if not self.isEmpty() else -1

    def getRear(self) -> int:
        return self.deq[-1] if not self.isEmpty() else -1

    def length(self) -> int:
        return len(self.deq)

    def isEmpty(self) -> bool:
        return self.length() == 0

    def isFull(self) -> bool:
        return self.length() == self.size
