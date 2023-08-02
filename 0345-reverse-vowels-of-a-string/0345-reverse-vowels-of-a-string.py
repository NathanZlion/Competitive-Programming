
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel_set = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        lst_str = list(s)
        indices = []
        vowels = []

        for index, char in enumerate(lst_str):
            # check if char is vowel
            if char in vowel_set:
                indices.append(index)
                vowels.append(char)

        for index in indices:
            lst_str[index] = vowels.pop()
            
        return ''.join(lst_str)
