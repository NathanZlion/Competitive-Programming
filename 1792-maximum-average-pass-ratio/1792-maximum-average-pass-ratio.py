class Solution:
    def delta(self, numerator: int, denominator: int) -> float:
        """
        delta change:  (y-x)
                      -------
                       y(y+1)
        """
        # avoid division by zero error
        if denominator == 0 or denominator == 1:
            return 0

        return (denominator - numerator) / (denominator * (denominator - 1))
    
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        heap = [(-self.delta(num, deno), (num, deno)) for num, deno in classes]
        heapify(heap)
        
        for _ in range(extraStudents):
            _, (num, deno) = heappop(heap)
            heappush(heap, (-self.delta(num + 1, deno + 1), (num + 1, deno + 1)))
        
        maximizedAverage = sum([num / deno for (_, (num, deno)) in heap]) / len(classes)
        return maximizedAverage
        