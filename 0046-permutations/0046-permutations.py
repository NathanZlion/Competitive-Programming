class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:        
        possible_permutations = []
        
        def permutation(arr: List[int] = [], added: set = set()) -> None:
            if len(arr) == len(nums):
                possible_permutations.append(arr.copy())

            for num in nums:
                if num not in added:
                    arr.append(num)
                    added.add(num)
                    permutation(arr, added)
                    arr.pop()
                    added.remove(num)


        permutation()

        return possible_permutations