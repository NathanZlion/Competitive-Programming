class Solution:
    def maxLength(self, arr: List[str]) -> int:

        bit_alphabet = 0
        max_len = 0

        def backTrack(index):
            nonlocal bit_alphabet
            nonlocal max_len

            if index == len(arr):
                max_len = max(bit_alphabet.bit_count() , max_len)
                return

            unique = True
            curr_bit_count = 0
            for char in arr[index]:
                if curr_bit_count & 1<<ord(char)-97:
                    unique = False
                    break
                curr_bit_count += 1<<ord(char)-97
            
            if unique and bit_alphabet & curr_bit_count == 0:
                temp = bit_alphabet
                bit_alphabet = bit_alphabet | curr_bit_count
                backTrack(index+1)
                bit_alphabet = temp

            backTrack(index+1)


        backTrack(0)

        return max_len