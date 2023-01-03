class Solution(object):
    def printVertically(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        words_lst = s.split()
        total_words = len(words_lst)

        acc = defaultdict(list)

        for word_index in range(total_words):
            word = words_lst[word_index]
            word_len = len(word)

            for char_idx in range(word_len):
                char = word[char_idx]

                while len(acc[char_idx]) < word_index:
                    acc[char_idx].append(" ")

                acc[char_idx].append(char)

        res = []
        for index in range(len(acc)):
            res.append("".join(acc[index]))
        
        return res
