class Solution(object):
    def countPairs(self, deliciousness):
        """
        :type deliciousness: List[int]
        :rtype: int
        """

        powers = set([2**x for x in range(22)])

        ctr = 0
        count = collections.Counter()

        for x in deliciousness:
            for y in powers:
                target = y - x

                if target in count:
                    ctr += count[target]

            count[x] += 1

        return ctr % (pow(10,9) + 7)
