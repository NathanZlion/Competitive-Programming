class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        right = 0
        max_len = 0
        dictionary={}
        while right < len(fruits):
            dictionary[fruits[right]]=right
            if len(dictionary) > 2:
                min_val = min(dictionary.values())
                del dictionary[fruits[min_val]]
                left = min_val+1
            max_len = max(max_len,right-left+1)
            right += 1

        return max_len
