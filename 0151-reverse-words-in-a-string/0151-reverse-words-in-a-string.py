class Solution:
    def reverseWords(self, s: str) -> str:
        word_list = s.split()
        total_words = len(word_list)
        middle = len(word_list)//2

        for index in range(middle):
            word_list[index], word_list[total_words - index - 1] =  word_list[total_words - index - 1] ,  word_list[index]
        
        return ' '.join(word_list)