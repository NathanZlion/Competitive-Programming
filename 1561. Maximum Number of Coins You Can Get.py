class Solution(object):
    def maxCoins(self, piles):
        piles.sort(reverse = True)

        res = 0
        index = 1

        for i in range(len(piles)//3):
            res += piles[index]
            index += 2
        
        return res
