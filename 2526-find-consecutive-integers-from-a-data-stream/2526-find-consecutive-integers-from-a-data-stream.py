class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.size = k
        self.queue = deque()
        self.count = 0

    def consec(self, num: int) -> bool:
        if num == self.value:
            self.count += 1
        self.queue.append(num)

        if len(self.queue) > self.size:
            if self.queue.popleft() == self.value:
                self.count -= 1

        return self.count == self.size
