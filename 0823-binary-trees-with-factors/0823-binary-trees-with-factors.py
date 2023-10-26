class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        modulus = 10**9 + 7
        arr.sort(reverse = True)
        arr_set = set(arr)
        n = len(arr)
        memo = defaultdict(lambda: 0)

        for curr_index in range(n-1, -1, -1):
            curr_num = arr[curr_index]
            for next_index in range(curr_index, n):
                num1 = arr[next_index]
                if curr_num % num1 == 0:
                    num2 = curr_num // num1
                    memo[curr_num] += (memo[num2] * memo[num1])
            
            memo[curr_num] += 1

        return sum(memo.values()) % modulus