class Solution:
    def customSortString(self, order: str, s: str) -> str:
        orderDict = {char: index for index, char in enumerate(order)}
        heap = [] # minheap
        
        for char in s:
            heappush(heap, (orderDict.get(char, -1), char))
        
        chars = [(char, orderDict.get(char, -1)) for char in s]
        chars.sort(key=lambda x: x[1])
        
        return "".join([char[0] for char in chars])
