class Solution:
    def customSortString(self, order: str, s: str) -> str:
        orderDict = {char: index for index, char in enumerate(order)}
        heap = [] # minheap
        
        for char in s:
            heappush(heap, (orderDict.get(char, -1), char))
        
        res = []
        while heap:
            _, char = heappop(heap)
            res.append(char)
        
        return "".join(res)
