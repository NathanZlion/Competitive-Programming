class Solution:
    def total_length(self, arr):
        res= 0
        for word in arr:
            res += len(word)
        return res

    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        word1_char_length = self.total_length(word1)
        word2_char_length = self.total_length(word2)
        
        if word1_char_length != word2_char_length:
            return False
        
        word1_word_ptr = 0
        word1_char_ptr = 0
        word2_word_ptr = 0
        word2_char_ptr = 0
        for _ in range(word1_char_length):
            if word1_char_ptr >= len(word1[word1_word_ptr]):
                word1_char_ptr = 0
                word1_word_ptr += 1
            
            if word2_char_ptr >= len(word2[word2_word_ptr]):
                word2_char_ptr = 0
                word2_word_ptr += 1
            
            if word1[word1_word_ptr][word1_char_ptr] != word2[word2_word_ptr][word2_char_ptr]:
                return False
            
            word1_char_ptr += 1
            word2_char_ptr += 1

        return True
