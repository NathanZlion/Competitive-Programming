class Solution:

    def quickSelect(self, left, right, nums, k):
        
        # select random number and swap with the first index
        random_pivot_index = random.randint(left, right)
        nums[random_pivot_index], nums[left] = nums[left], nums[random_pivot_index]
        pivot = nums[left]
        write = left + 1

        for read in range(left+1, right+1):
            if nums[read] <= pivot:
                nums[write], nums[read] = nums[read], nums[write]
                write += 1
        nums[left], nums[write-1] = nums[write-1], nums[left]

        if write-1 == len(nums)-k:
            return nums[write-1]

        if len(nums)-k > write -1:
            return self.quickSelect(write, right, nums, k)
        return self.quickSelect(left, write-2, nums, k)        

    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quickSelect(0, len(nums)-1, nums, k)
