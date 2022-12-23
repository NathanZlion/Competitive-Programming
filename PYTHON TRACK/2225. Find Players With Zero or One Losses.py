class Solution(object):

    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """

        loss = {}

        for match in matches:
            for team in match:
                loss[team] = 0
                loss[team] = 0

        for match in matches:
            loss[match[1]] += 1

        noLoss = []
        oneLoss = []

        for key in loss:
            if loss[key] == 1:
                oneLoss.append(key)
                
            elif loss[key] == 0:
                noLoss.append(key)

        noLoss.sort()
        oneLoss.sort()

        return [noLoss, oneLoss]
