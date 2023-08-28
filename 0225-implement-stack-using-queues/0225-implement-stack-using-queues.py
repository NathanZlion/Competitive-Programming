class MyStack:
    """Uses standard operations of a queue, push to back and peeks/pops from front"""
    def __init__(self):
        self.primaryQueue = deque()
        self.secondaryQueue = deque()
        self.length = 0
        """
        I am thinking when you push you do a normal operation, add to the end.
        But when you pop. You have to pop from the other end all the way to the
        last number. then hold that and reorganize the original one by pushing.
        """

    def push(self, x: int) -> None:
        self.primaryQueue.append(x)
        self.length += 1

    def pop(self) -> int:
        while self.primaryQueue:
            self.secondaryQueue.append(self.primaryQueue.popleft())

        while len(self.secondaryQueue) > 1:
            self.primaryQueue.append(self.secondaryQueue.popleft())

        self.length -= 1
        return self.secondaryQueue.popleft()
        
    def top(self) -> int:
        return self.primaryQueue[-1]        

    def empty(self) -> bool:
        return len(self) == 0

    def __len__(self) -> int:
        return self.length
        

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()