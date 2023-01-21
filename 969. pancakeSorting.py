class Solution(object):
    def pancakeSort(self, arr):
        res=[]
        currEnd = len(arr)
        while currEnd > 1:
            currMaxIndex = arr.index(max(arr[:currEnd]))

            if currMaxIndex == 0:
                res.append(currEnd)
                arr[:currEnd]=arr[:currEnd][::-1]

            elif currMaxIndex == currEnd -1:
                pass

            else:
                res.append(currMaxIndex +1)
                arr[:currMaxIndex+1] = arr[:currMaxIndex+1][::-1]
                res.append(currEnd)
                arr[:currEnd] = arr[:currEnd][::-1]
            currEnd-=1


        return res
