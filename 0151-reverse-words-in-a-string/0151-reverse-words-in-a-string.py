class Solution:
    def reverseWords(self, s: str) -> str:
        word_list = s.split()
        total_words = len(word_list)
        middle = len(word_list)//2

        for left in range(middle):
            right = total_words - left - 1
            word_list[left], word_list[right] =  word_list[right] ,  word_list[left]

        return ' '.join(word_list)