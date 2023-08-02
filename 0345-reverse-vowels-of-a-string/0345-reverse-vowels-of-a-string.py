import re

class Solution:
    def reverseVowels(self, s: str) -> str:
        lst_str = list(s)
        indices = []
        vowels = []

        for index, char in enumerate(lst_str):
            # check if char is vowel
            if re.match(r'[aeiouAEIOU]', char):
                indices.append(index)
                vowels.append(char)

        for index in indices:
            lst_str[index] = vowels.pop()
            
        return ''.join(lst_str)