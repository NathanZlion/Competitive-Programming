class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        max_divisor_end = -1
        len_str1 = len(str1)
        len_str2 = len(str2)
        
        def is_divisor(str1, str2, end):
            for index in range(max(len_str1, len_str2)):
                target = index % (end + 1)

                if str1[target] != str1[index % len_str1]:
                    return False

                if str1[target] != str2[index % len_str2]:
                    return False
            
            return True

        for end in range(min(len_str1, len_str2)):
            if str1[end] != str2[end]:
                break
            
            if len_str1 % (end + 1) == len_str2 % (end + 1) == 0 and is_divisor(str1, str2, end):
                max_divisor_end = end

        return str1[:max_divisor_end+1]