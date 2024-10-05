class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = { item : index + 1 for index, item in enumerate(sorted(list(set(arr))))}
        return [rank[item] for item in arr]
