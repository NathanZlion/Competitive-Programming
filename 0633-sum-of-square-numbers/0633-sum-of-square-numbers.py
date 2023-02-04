class Solution(object):
    def squareSum(self, a, b):
        return a**2 + b**2

    def judgeSquareSum(self, c):
        for a in range(int(math.sqrt(c)) + 1):
            left, right = 0, int(math.sqrt(c - a * a))

            while left <= right:
                mid = (left + right) // 2
                sumSq = self.squareSum(mid, a)

                if sumSq == c:
                    return True

                elif sumSq < c:
                    left = mid + 1

                else:
                    right = mid - 1

        return False