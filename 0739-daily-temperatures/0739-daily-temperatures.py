class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        greater = [0 for _ in range(len(temperatures))]

        for index in range(len(temperatures)-1, -1, -1):
            temperature = temperatures[index]

            while stack and stack[-1][0] <= temperature:
                stack.pop()

            if stack:
                greater[index] = (stack[-1][1] - index)

            stack.append([temperature, index])

        return greater
