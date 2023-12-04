class Solution:
    def largestGoodInteger(self, num: str) -> str:

        max_num = -1
        for i in range(len(num) - 2):
            substring = num[i:i+3]

            if len(set(substring)) == 1:
                max_num = max(max_num, int(substring))
            
        return "" if max_num == -1 else ("0" * (3 - len(str(max_num)))) + str(max_num)
