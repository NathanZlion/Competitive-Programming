class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        prefixSum = [0 for _ in range(n+1)]
        for i in range(n):
            prefixSum[i+1] = prefixSum[i]^arr[i]
        
        result = []
        for left, right in queries:
            result.append(prefixSum[right+1] ^ prefixSum[left])
        return result
