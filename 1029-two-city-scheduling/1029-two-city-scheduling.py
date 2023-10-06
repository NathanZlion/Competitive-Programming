
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        totalPeople = len(costs)

        @cache
        def dp(index: int, leftA: int, leftB: int):
            if leftA < 0 or leftB < 0:
                return inf

            if index == totalPeople:
                return 0

            costOfA, costOfB = costs[index]

            # choose to send to City A or City B
            return min(
                costOfA + dp(index + 1, leftA - 1, leftB),
                costOfB + dp(index + 1, leftA, leftB - 1),
            )

        return dp(0, totalPeople//2, totalPeople//2)
    