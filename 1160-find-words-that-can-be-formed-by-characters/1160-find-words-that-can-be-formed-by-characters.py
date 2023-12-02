class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = Counter(chars)
        sum_of_len = 0

        for word in words:
            can_be_formed = True
            char_count = Counter(word)

            for char in char_count:
                if char_count[char] > count[char]:
                    can_be_formed = False
                    break

            if can_be_formed:
                sum_of_len += len(word)

        return sum_of_len
