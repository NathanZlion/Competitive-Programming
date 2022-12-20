class Solution:
    def longestCommonPrefix(self, strs):
        prefix = ""
        index = 0

        if "" in strs:
            return ""

        capable = True
        while capable:
            char = strs[0][index]
            same = True

            for items in strs:
                if index == len(items) -1:
                    capable = False
                if items[index] != char:
                    same = False
                    break

            if same:
                prefix += char
            else:
                break
            index += 1

        return prefix
