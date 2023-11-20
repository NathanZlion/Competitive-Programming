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
            
            del count

        # do a prefix sum of the traverl time
        travel_cost = [0 for _ in range(n)]
        for i in range(n-1):
            travel_cost[i+1] += (travel[i] + travel_cost[i])

        metal_minutes = travel_cost[right_metal_index] + metal_count
        glass_minutes = travel_cost[right_glass_index] + glass_count
        paper_minutes = travel_cost[right_paper_index] + paper_count
        
        return metal_minutes + glass_minutes + paper_minutes
