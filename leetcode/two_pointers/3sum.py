class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        result = []
        nums.sort()
        
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:
                left = i + 1
                right = len(nums) - 1
                while left < right:
                    target = nums[i] + nums[left] + nums[right]
                    if target > 0:
                        right -= 1
                    elif target < 0:
                        left += 1
                    else:
                        result.append([nums[i], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        left += 1
                        right -= 1
        
        return result