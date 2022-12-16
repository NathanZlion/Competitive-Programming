class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        """
        Flip to get the maximum number to the end.

        1. get the index of the maximum number in the index [0:currend]
        2. if it is 0: flip to current end
           else if it is one minus current end
           else:
               flip it to the index and again flip it to the current end
        3. move currend one step back
        ___loop to 1
        4. end if the current end is lessthan or equal to 1.
        """

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








                

