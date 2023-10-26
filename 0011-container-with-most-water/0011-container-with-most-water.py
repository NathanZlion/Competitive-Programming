class Solution:
    def maxArea(self, height: List[int]) -> int:

        n = len(height)
        left_ptr, right_ptr = 0, n-1
        max_area = 0
        
        while right_ptr > left_ptr:
            left_height, right_height = height[left_ptr], height[right_ptr]
            curr_area = min(left_height, right_height) * (right_ptr - left_ptr)
            max_area = max(max_area, curr_area)

            if left_height < right_height:
                left_ptr += 1
            else:
                right_ptr -= 1

        return max_area
