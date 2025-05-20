from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            distance = right - left
            if height[left] < height[right]:
                height_value = height[left]
                left += 1
            else:
                height_value = height[right]
                right -= 1
            
            area = distance * height_value
            max_area = max(max_area, area)

        return max_area