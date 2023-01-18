class Solution(object):
    def commonChars(self, words):
        counts = []

        for word in words:
            count = [0] * 26

            for char in word:
                count[ord(char) - 97] += 1
            counts.append(count)
        
        common = []

        for j in range(len(counts[0])):
            min_count = float("inf")

            for i in range(len(counts)):
                min_count = min(min_count, counts[i][j])

            for count in range(min_count):
                common.append(chr(j + 97))

        return common
