class Solution:
    '''
    turn => true: player1, false: player2
    player1: maximizes max()  positive
    player2: minimizes min()  negates the score
    '''
    def play(self, left, right, nums, score = 0, turn = True):
        if left == right:
            return nums[left]

        # its player 1's turn
        if turn:
            # choose the maximum of left and right
            choice1 = self.play(left+1, right, nums, score+nums[left], not turn)
            choice2 = self.play(left, right-1, nums, score+nums[right], not turn)

            return max(nums[left] + choice1, nums[right] + choice2)

        # its player 2's turn
        # choose the minimum of negated left and right
        choice1 = self.play(left+1, right, nums, score+nums[left], not turn)
        choice2 = self.play(left, right-1, nums, score+nums[right], not turn)

        return min(choice1 - nums[left], choice2 - nums[right])


    def PredictTheWinner(self, nums: List[int]) -> bool:
        return self.play(left = 0, right = len(nums)-1, nums = nums, score = 0, turn = True) >= 0

