from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort the array in ascending order
        n = len(nums)
        triplets = []

        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue  # Skip duplicate elements

            left = i+1
            right = n-1

            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]

                if curr_sum == 0:  # Found a valid triplet
                    triplets.append([nums[i], nums[left], nums[right]])

                    # Skip duplicate elements
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1

                    # Move the pointers
                    left += 1
                    right -= 1

                elif curr_sum < 0:
                    left += 1  # Sum is too small, move left pointer

                else:
                    right -= 1  # Sum is too large, move right pointer

        return triplets
