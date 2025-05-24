# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

# Return the max sliding window.

 

# Example 1:

# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation: 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]

from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()

        for i in range(len(nums)):
            while q and q[0] < i - k + 1: # check if the first index in the deque is out of the window compared to the current index
                q.popleft()
            # check if the last value of the index in the deque is less than the current number, we only keep higher values in the first part of the deque
            # deque only has max value for the current window as the first element
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            
            q.append(i)

            # when we have the first k elements, we can start adding the max value of the window to the result, the first element of the deque is akways the max value of the current window
            if i >= k - 1:
                res.append(nums[q[0]])
        
        return res