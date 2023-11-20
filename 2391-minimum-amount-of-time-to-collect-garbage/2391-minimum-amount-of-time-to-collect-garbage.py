from collections import Counter

class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        n = len(garbage)

        right_most_position = {
            "M": 0,
            "G": 0,
            "P": 0
        }

        metal_count = paper_count = glass_count = 0
        
        for index, garb in enumerate(garbage):
            count = Counter(garb)
            glass_count += count["G"]
            paper_count += count["P"]
            metal_count += count["M"]

            right_most_position["G"] = index if count["G"] else right_most_position["G"]
            right_most_position["M"] = index if count["M"] else right_most_position["M"]
            right_most_position["P"] = index if count["P"] else right_most_position["P"]

        # do a prefix sum of the travel time
        for i in range(1, n-1):
            travel[i] += travel[i-1]

        travel.append(0)

        glass_minutes = travel[right_most_position["G"]-1] + glass_count
        metal_minutes = travel[right_most_position["M"]-1] + metal_count
        paper_minutes = travel[right_most_position["P"]-1] + paper_count
        
        return (metal_minutes + glass_minutes + paper_minutes)
