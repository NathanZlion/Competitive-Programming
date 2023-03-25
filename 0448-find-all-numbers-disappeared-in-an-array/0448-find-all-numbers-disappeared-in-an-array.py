class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        '''
        - - - - - 2 3 -
        1 2 3 4 0 0 7 8
        '''

        # collect all numbers in a deque
        # replace sorted numbers by number if the number is 0
        # return the lost of `index+1` for all 0 place holders

        n = len(nums)
        sorted_nums = [0 for _ in range(n)]
        
        for num in nums:
            sorted_nums[num-1] = num

        res = []
        for index in range(n):
            if sorted_nums[index] == 0:
                res.append(index+1)

        return res
        