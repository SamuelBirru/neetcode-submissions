class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hasmap = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff not in hasmap:
                hasmap[num] = i
            else:
                return[hasmap[diff], i]
                