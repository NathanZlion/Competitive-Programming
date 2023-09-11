class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:

        groups = []
        collector = defaultdict(list)
        for uid, groupSize in enumerate(groupSizes):
            collector[groupSize].append(uid)
            if collector[groupSize].__len__() == groupSize:
                groups.append(collector[groupSize])
                collector[groupSize] = []
        
        return groups