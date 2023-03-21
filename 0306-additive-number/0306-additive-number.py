class Solution:
    def isAdditiveNumber(self, num: str) -> bool:

        def backTrack(lst, index):

            if len(lst)>2 and lst[-1] != (lst[-2]+lst[-3]):
                return False

            if index == len(num):
                return True if len(lst) > 2 else False

            if num[index] == 0:
                return False

            for end in range(index+1, len(num)+1):
                lst.append(int(num[index:end]))

                if backTrack(lst, end):
                    return True and (num[index:end][0] != '0' or len(num[index:end]) == 1)

                lst.pop()

            return False

        return backTrack([], 0)
