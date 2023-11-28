class Solution:
    def numberOfWays(self, corridor: str) -> int:
        # Store 1000000007 in a variable for convenience
        MOD = 1_000_000_007

        # Initialize the array to store the result of each sub-problem
        count = [[-1] * 3 for _ in range(len(corridor) + 1)]

        # Base cases
        count[len(corridor)][0] = 0
        count[len(corridor)][1] = 0
        count[len(corridor)][2] = 1

        # Fill the array in a bottom-up fashion
        for index in range(len(corridor) - 1, -1, -1):
            if corridor[index] == "S":
                count[index][0] = count[index + 1][1]
                count[index][1] = count[index + 1][2]
                count[index][2] = count[index + 1][1]
            else:
                count[index][0] = count[index + 1][0]
                count[index][1] = count[index + 1][1]
                count[index][2] = (count[index + 1][0] + count[index + 1][2]) % MOD

        # Return the result
        return count[0][0]