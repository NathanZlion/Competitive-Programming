class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        tempAmount = len(temperatures)
        output = [0] * tempAmount
        stack = []

        for index, currTemp in enumerate(temperatures):
            while stack and (currTemp > temperatures[stack[-1]]):
                stackIndex = stack.pop()
                output[stackIndex] = (index - stackIndex)
            stack.append(index)

        return output
