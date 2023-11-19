class Solution:
    def reductionOperations(self, nums: List[int]) -> int:

        nums = Counter(nums)
        nums = [(-num, count) for num, count in nums.items()]

        heapify(nums)
        operations_count = 0

        while nums.__len__() > 1:
            largest_num, first_count = heappop(nums)
            next_largest_num, next_count = heappop(nums)
            
            operations_count += first_count
            heappush(nums, (next_largest_num, first_count + next_count))
        
        return operations_count