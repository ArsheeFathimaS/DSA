class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        hills = valleys = 0

        for i in range(1, len(nums) - 1):
            # Skip current if it's same as the previous
            if nums[i] == nums[i - 1]:
                continue

            # Move left pointer to closest non-equal element
            left = i - 1
            while left >= 0 and nums[left] == nums[i]:
                left -= 1

            # Move right pointer to closest non-equal element
            right = i + 1
            while right < len(nums) and nums[right] == nums[i]:
                right += 1

            # Now check hill/valley only if valid neighbors exist
            if left >= 0 and right < len(nums):
                if nums[i] > nums[left] and nums[i] > nums[right]:
                    hills += 1
                elif nums[i] < nums[left] and nums[i] < nums[right]:
                    valleys += 1

        return hills + valleys
