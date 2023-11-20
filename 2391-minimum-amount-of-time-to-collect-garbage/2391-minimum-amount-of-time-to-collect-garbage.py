from collections import Counter

class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        n = len(garbage)

        right_metal_index = right_paper_index = right_glass_index = 0
        metal_count = paper_count = glass_count = 0
        
        for index, garb in enumerate(garbage):
            count = Counter(garb)
            glass_count += count["G"]
            paper_count += count["P"]
            metal_count += count["M"]
            
            if count["G"]:
                right_glass_index = index

            if count["P"]:
                right_paper_index = index

            if count["M"]:
                right_metal_index = index

        # do a prefix sum of the travel time
        for i in range(1, n-1):
            travel[i] += travel[i-1]

        travel.append(0)

        metal_minutes = travel[right_metal_index-1] + metal_count
        glass_minutes = travel[right_glass_index-1] + glass_count
        paper_minutes = travel[right_paper_index-1] + paper_count
        
        return metal_minutes + glass_minutes + paper_minutes
