class Solution(object):
    def partitionLabels(self, s):
        partitions  = {}
        n = len(s)

        for i in range(n):
            char = s[i]
            start, end = i, i
            if not char in partitions.keys():
                for i in range(i,n):
                    if s[i] == char:
                        end = i
                partitions[char] = [start, end]

        ds = sorted(partitions.values(), key = lambda x:x[0])

        merged = []
        prev = ds[0]
        index = 1
        merged.append(prev)

        while index < len(ds):
            curr = ds[index]
            print(curr)
            print(prev)
            if curr[0] < prev[1]:
                if curr[1] > prev[1]:
                    prev = [prev[0], curr[1]]
                    merged.pop()
                    merged.append(prev)
            else:
                merged.append(curr)
                prev = curr
            index += 1

        res = []
        for part in merged:
            res.append(part[1]-part[0]+1)

        return res

