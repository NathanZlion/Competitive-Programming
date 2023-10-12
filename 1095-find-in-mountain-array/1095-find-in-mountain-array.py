# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        N = mountain_arr.length()

        # binary search
        def find_peak_of_mount_arr(mount_arr: 'MountainArray') -> int:
            nonlocal N
            left, right = -1, N
            
            while right > left + 1:
                mid = (left + right) // 2
                mid_val = mount_arr.get(mid)
                has_left = (mid > 0)
                
                if has_left and mid_val < mount_arr.get(mid-1):
                    right = mid
                else:
                    left = mid
            
            return max(left, 0)


        def find_target(mount_arr: 'MountainArray', l: int, r: int, isInc: bool, target: int) -> int:
            left = l
            right = r
            
            while left + 1 < right:
                mid = (left + right) // 2
                mid_val = mount_arr.get(mid)
                
                if (isInc and mid_val > target) or (not isInc and mid_val < target):
                    right = mid
                else:
                    left = mid
                
            if left != l and mount_arr.get(left) == target:
                return left
            
            return -1
            

        peakIdx = find_peak_of_mount_arr(mountain_arr)
        left_half_res = find_target(mountain_arr, -1, peakIdx + 1, True, target)

        return left_half_res if left_half_res != -1 else find_target(mountain_arr, peakIdx-1, N, False, target)