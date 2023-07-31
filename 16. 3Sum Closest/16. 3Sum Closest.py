from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = float('inf')
        n = len(nums)

        for i in range(n - 2):
            left = i + 1
            right = n - 1

            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]

                if curr_sum == target:  # Found exact sum, return result
                    return curr_sum

                if abs(target - curr_sum) < abs(target - closest_sum):
                    closest_sum = curr_sum

                if curr_sum < target:
                    left += 1  # Sum is too small, move left pointer

                else:
                    right -= 1  # Sum is too big, move right pointer

        return closest_sum
