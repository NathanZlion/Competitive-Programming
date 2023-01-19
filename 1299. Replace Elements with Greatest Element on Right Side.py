class Solution(object):
    def replaceElements(self, arr):

        n = len(arr)

        prevMax = arr[-1]

        for index in range(n-2,-1,-1):
            currNum = arr[index]
            arr[index] = prevMax
            prevMax = max(currNum, prevMax)


        arr.pop()
        arr.append(-1)

        return arr
