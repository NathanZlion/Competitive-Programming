class RandomizedSet:

    def __init__(self):
        self.nums_set = set()

    def insert(self, val: int) -> bool:
        if val not in self.nums_set:
            self.nums_set.add(val)
            return True

        return False

    def remove(self, val: int) -> bool:
        if val in self.nums_set:
            self.nums_set.remove(val)
            return True
        
        return False

    def getRandom(self) -> int:
        n = len(self.nums_set)
        count = random.randint(0, n - 1)

        for num in self.nums_set:
            if count == 0:
                return num

            count -= 1

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()