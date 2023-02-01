class Solution(object):
    def duplicateZeros(self, arr):
        length = len(arr)
        i = 0
        while i < length:
            if arr[i] == 0:
                arr.insert(i, 0)
                i += 2
                continue
            i += 1

        newLength = len(arr)

        for _ in range(newLength - length):
            arr.pop()

