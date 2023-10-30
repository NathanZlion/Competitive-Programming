class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        OFFSET = 1950
        pref_sum = [0 for _ in range(2050 - 1950 + 1)]

        for birth, death in logs:
            pref_sum[birth - OFFSET] +=  1
            pref_sum[death - OFFSET] -=  1
        
        for index in range(1, 2050 - 1950 + 1):
            pref_sum[index] += pref_sum[index-1]

        max_year, max_population = -1, -1
        for year, population in enumerate(pref_sum):
            if population > max_population:
                max_population = population
                max_year = year + OFFSET
        
        return max_year
