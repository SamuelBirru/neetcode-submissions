class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = list(set(nums))  # Remove duplicates
        nums.sort()

        longest = 1
        current_streak = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                current_streak += 1
                longest = max(longest, current_streak)
            else:
                current_streak = 1

        return longest
        