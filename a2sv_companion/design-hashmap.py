class MyHashMap:
    def __init__(self):
        self._map = {}

    def put(self, key: int, value: int) -> None:
        self._map[key] = value

    def get(self, key: int) -> int:
        if key in self._map:
            return self._map[key]

        return -1

    def remove(self, key: int) -> None:
        if key in self._map:
            del self._map[key]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)