
class Solution(object):
    def minDeletionSize(self, strs):

        cols = defaultdict(list)

        for str_index in range(len(strs)):
            str_ = strs[str_index]

            for char_index in range(len(str_)):
                char = str_[char_index]
                cols[char_index].append(char)

        deleted = 0
        for col_num in cols.keys():
            index = 0
            col = cols[col_num]

            while index < len(col)-1:
                if col[index] > col[index +1]:
                    deleted += 1
                    break

                index += 1


        return deleted

