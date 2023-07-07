class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n = len(answerKey)
        maximumNumOfConsec = 0

        # traverse to maximize consecutive F
        operationsLeft = k
        left = 0
        for right in range(n):
            if answerKey[right] == "T":
                operationsLeft -= 1

            while operationsLeft < 0:
                if answerKey[left] == "T":
                    operationsLeft += 1

                left += 1

            maximumNumOfConsec = max(maximumNumOfConsec, right - left + 1)

        # traverse to maximize for consecutive T
        operationsLeft = k
        left = 0
        for right in range(n):
            if answerKey[right] == "F":
                operationsLeft -= 1

            while operationsLeft < 0:
                if answerKey[left] == "F":
                    operationsLeft += 1

                left += 1

            maximumNumOfConsec = max(maximumNumOfConsec, right - left + 1)

        return maximumNumOfConsec