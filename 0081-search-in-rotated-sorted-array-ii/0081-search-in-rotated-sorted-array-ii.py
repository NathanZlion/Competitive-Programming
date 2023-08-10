class Solution:
    
    @staticmethod
    def isBinarySearchHelpful(arr:list[int], left:int, mid:int) -> bool:
        return arr[left] != arr[mid]

    @staticmethod
    def existsInLeftHalf(arr: list[int], left: int, element:int) -> bool:
        return arr[left] <= element

    def search(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums) - 1

        while right >= left:
            mid = (right + left) // 2
            if nums[mid] == target:
                return True

            if not Solution.isBinarySearchHelpful(nums, left, mid):
                left += 1
                continue
            
            midInLeftHalf = Solution.existsInLeftHalf(nums, left, nums[mid])
            targetInLeftHalf = Solution.existsInLeftHalf(nums, left, target)
            
            # if mid element and target are in different halfs
            if  midInLeftHalf ^ targetInLeftHalf:
                if midInLeftHalf:
                    left = mid + 1
                else:
                    right = mid - 1
            # target and mid element found in same half
            else:
                if target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return False