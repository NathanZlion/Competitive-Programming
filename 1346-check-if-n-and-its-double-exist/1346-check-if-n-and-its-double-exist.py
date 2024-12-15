class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        _nums = Counter(arr)
        
        for num in arr:
            if num % 2 == 0:
                if num != 0 and num//2 in _nums:
                    return True
        
        return _nums[0] > 1
        