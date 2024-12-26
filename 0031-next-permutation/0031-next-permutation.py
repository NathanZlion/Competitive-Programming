class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        modified = False
        length = len(nums)
        
        # try finding the next bigger permutation
        for index in range(length - 2, -1, -1):
            if nums[index] >= nums[index + 1]:
                maxNumToRight = nums[index]
                continue
            
            modified = True
            # find the immediate smallest num to the right
            # with binary search
            left = index
            right = length
            
            while right > left + 1:
                mid = (right + left) // 2
                if nums[mid] > nums[index]:
                    left = mid
                else:
                    right = mid

            # immediate larger element is at index left
            nums[left], nums[index] = nums[index], nums[left]
            
            # make sure the side from index + 1 to end is minimum            
            for offset, num in enumerate(sorted(nums[index+1:])):
                nums[offset + index + 1] = num
            
            modified = True
            break
            
        # means the arrary is sorted in reverse order
        if not modified:
            for index in range(length // 2):
                nums[index], nums[length - index - 1] = nums[length - index - 1], nums[index]
