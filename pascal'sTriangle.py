class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        # construct the 2d array
        TwoDarr =[]
        
        for i in range(numRows):
            list = [1] * (i +1)

            for j in range(i):
                if j == 0 or i == j:
                    continue
                else:
                    list[j] = TwoDarr[i-1][j] + TwoDarr[i-1][j-1]
            TwoDarr.append(list)

        return TwoDarr
