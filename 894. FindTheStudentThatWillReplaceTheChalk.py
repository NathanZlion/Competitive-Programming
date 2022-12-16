class Solution(object):
    def chalkReplacer(self, chalk, k):
        """
        :type chalk: List[int]
        :type k: int represents the total number of chalks the teacher possesses
        :rtype: int
        """
        k%=sum(chalk)
        if k == 0: return 0

        preSum = 0
        for index, c in enumerate(chalk):
            preSum+=c
            if preSum>k:
                return index
