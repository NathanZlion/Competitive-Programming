class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        xorPrefix = [0] * (n + 1)

        for index, num in enumerate(arr):
            xorPrefix[index] = arr[index] ^ xorPrefix[index-1]

        return [xorPrefix[right] ^ xorPrefix[left - 1] for [left, right] in queries]
