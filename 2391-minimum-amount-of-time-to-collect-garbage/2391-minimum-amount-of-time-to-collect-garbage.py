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
        travel_time = [0 for _ in range(n)]
        for i in range(n-1):
            travel_time[i+1] += (travel[i] + travel_time[i])

        metal_minutes = travel_time[right_metal_index] + metal_count
        glass_minutes = travel_time[right_glass_index] + glass_count
        paper_minutes = travel_time[right_paper_index] + paper_count
        
        return metal_minutes + glass_minutes + paper_minutes
