class DetectSquares:

    def __init__(self):
        self.freq = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.freq[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        count = 0
        x1, y1 = point
        
        for (x2, y2) in list(self.freq.keys()):
            point2 = (x2, y2)
            if y1 == y2 and x1 != x2:
                dce = x1 - x2
                point3 = (x1, y1 - dce)
                point4 = (x2, y1 - dce)
                point5 = (x1, y1 + dce)
                point6 = (x2, y1 + dce)

                count += (self.freq[point2] * self.freq[point3] * self.freq[point4])
                count += (self.freq[point2] * self.freq[point5] * self.freq[point6])

        return count


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)