from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []

        nums.sort()  # Sorting the array

        quadruplets = []
        n = len(nums)

        for i in range(n - 3):
            # Skip duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):
                # Skip duplicates
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                left = j + 1
                right = n - 1

                while left < right:
                    # Calculate the sum
                    curr_sum = nums[i] + nums[j] + nums[left] + nums[right]

                    if curr_sum == target:
                        quadruplets.append([nums[i], nums[j], nums[left], nums[right]])

                        # Skip duplicates
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1

                        # Move the pointers
                        left += 1
                        right -= 1
                    elif curr_sum < target:
                        left += 1
                    else:
                        right -= 1

        return quadruplets
