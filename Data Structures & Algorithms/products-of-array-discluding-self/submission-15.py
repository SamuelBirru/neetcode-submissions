class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        pre = 1
        post = 1
        for i in range(len(nums)):
            output[i] = pre
            pre = pre * nums[i]

        for r in range(len(nums) -1, -1, -1):
            output[r] *= post
            post = post * nums[r]
        return output