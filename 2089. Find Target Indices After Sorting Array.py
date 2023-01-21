class Solution(object):
    def targetIndices(self, nums, target):

        counter = [0 for i in range(101)]

        for num in nums:
            counter[num] += 1
        
        startIndex = 0
        for i in range(target):
            startIndex += counter[i]

        return [j+startIndex for j in range(counter[target])]
